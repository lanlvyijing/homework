#coding=utf-8
from numpy import *
import matplotlib.pyplot as plt


A = dtype({'names': ['ai', 'tan', 'bn'], 'formats': ['i', 'i', 'int32']}, align = True)
B = dtype({'names': ['road_b','road_h', 'road_e', 'road_l'], 'formats': ['i','i', 'i', 'i']}, align = True)
C = dtype({'names': ['road_h', 'road_e', 'road_l'], 'formats': ['i', 'i', 'i']}, align = True)


def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines, 7), dtype = int)
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:7]
        classLabelVector.append(int(listFromLine[0]))
        index += 1
    return returnMat, classLabelVector    
    
    
def plotflight(dataset, place,priceline):
    weight = [30,20,30,40,50,40]
    height = [30,40,50,30,40,50]
    plt.style.use('fivethirtyeight')        
    cost = 0
    plt.ylim(15, 55)
    plt.xlim(20, 60) 
 
    for i in range(6):
        
        plt.text(height[i]+1, weight[i]+1, '%d'%(i+1), color='blue')   
        plt.plot(height[i], weight[i], 'ro')             

    for i in range(7):
       
        for j in range(1, i + 1):
            
            if dataset[i-1][j]<100 and dataset[i-1][j]>0:
                plt.text((height[i-1]+height[j-1])/2, (weight[i-1]+weight[j-1])/2, '%d'%dataset[i-1][j], color='black')
                plt.plot([height[i-1], height[j-1]], [weight[i-1], weight[j-1]], color='black', linewidth = 1)                                                                          
    for x in priceline:  
        weight_l = [weight[x['road_h']-1],weight[x['road_e']-1]]
        height_l = [height[x['road_h']-1],height[x['road_e']-1]]                  
        plt.plot(height_l, weight_l,color='red', linewidth = 10) 
        plt.text((height[x['road_h']-1]+height[x['road_e']-1])/2+2, (weight[x['road_h']-1]+weight[x['road_e']-1])/2-2, '%d'%x['road_l'], color='red', size = 30)
        cost+=x['road_l']  
        
    plt.title('flight cost : %d $ in total'% cost) 
    plt.show()

    return weight, height


def primgraph(startpoint,endpoint):
    #####################初始化信息读入航班数据###########################
    #the adding struct this turn
    reversmark=0
    if startpoint > endpoint:
        startpoint, endpoint=endpoint, startpoint
        reversmark=1
    dataset, place = file2matrix('flight_price.txt')
    An=[];ai=startpoint
    
    #####################寻找源点到第一个点###########################
    a = array([(startpoint, 0, 0)], dtype = A)    
    print "adding point = a%d ; Cheapest way to an = %d "%(a[0]['ai'], a[0]['tan'])
    An.append(a[0]['ai'])
    print "adding the v%d point to An: "%a[0]['ai'],An
    print ""   
     
    Nan_value = filter(lambda x: x < 100 and x > 0, dataset[a[0]['ai']-1][1:])    
    Nan_index=[]
    for x in Nan_value:
        if list(dataset[a[0]['ai']-1][1:]).index(x)+1 not in An:
            Nan_index.append(list(dataset[a[0]['ai']-1][1:]).index(x)+1)
    
    min_bni = min(Nan_value) 
    vi_index=list(dataset[a[0]['ai']-1][1:]).index(min_bni)+1
    print 'the nearest point is the %d point,the price is: %d $'%(vi_index, min_bni)
    a=vstack((a, array([(vi_index, min_bni , 0)], dtype=A)))
    An.append(vi_index)
    print "adding the v%d point to An: "%vi_index,An
    tni = array([(startpoint, vi_index , min_bni)], dtype=C)
    belong = array([(vi_index, startpoint, vi_index , min_bni)], dtype = B)
    print ""
    tvn=min_bni;
    
    #####################循环索引标注所有点###########################
    min_price_epoint=vi_index
    flag=2
    while endpoint != min_price_epoint:
        flag=flag+1
        min_price={}
        min_price_epoint=0
        min_price_fpoint=0
        min_price_ipoint=0
        min_path=10000;   
        
        for i in range(len(An)):
            Nan_value=[] 
            Nan_index=[]                
            dex = a[i]['ai'][0]-1                      
            for x in dataset[dex][1:]:
                if x>0 and x< 100 :
                    Nan_value.append(x)
                    Nan_value.sort()
            for x in Nan_value:
                if list(dataset[dex][1:]).index(x)+1 not in An:
                    Nan_index.append(list(dataset[dex][1:]).index(x)+1)
            
        #for i in range(len(An)):
            if len(Nan_index) > 0:
                if dataset[dex][Nan_index[0]]+a[i]['tan'] < min_path:                                         
                    min_path = dataset[dex][Nan_index[0]]
                    min_price_epoint=Nan_index[0]
                    min_price_fpoint=dex = dex+1
                    min_price_ipoint=i
            print "the new Cheapest path is %d,the new Cheapest point is from %d to %d"%(min_path,min_price_fpoint,min_price_epoint)                  
        
        tvn = a[min_price_ipoint]['tan']+min_path
        An.append(min_price_epoint)
        tni = vstack((tni, array([(min_price_fpoint,min_price_epoint, min_path)], dtype=C)))
        a=vstack((a, array([(min_price_epoint, tvn , 0)], dtype=A)))       
        print "adding the v%d point to An[]:"%min_price_epoint,An
        print ""
    print "tni = ",tni
    road = findroad(startpoint,endpoint,tni)
    if reversmark==1:   
        startpoint, endpoint=endpoint, startpoint
    print "the Cheapest way from %d to %d may cost you %d $ in total"%(startpoint,endpoint,tvn)    
    plotflight(dataset, place, road)


def findroad(start, end, tni):
    
    startpoint=0
    a = array([(0, 0, 0)], dtype = C)
    a[0] = tni[-1]
    
    startpoint = a['road_h']
    #print "x['road_l']:",a['road_l']
    flag=1
    while startpoint != start:
        lentni = len(tni)   
        if tni[-flag-1]['road_e'] == tni[-flag]['road_h']:
            startpoint=tni[-flag-1]['road_h']
            a = vstack((tni[lentni-flag-1],a))
            flag=flag+1
        else:
            tni = vstack((tni[:lentni-flag-1],tni[lentni-flag:]))
    
    print "the final path is :"    
    for x in a:
        print "take the flight from %d to %d, cost %d $"%(x['road_h'], x['road_e'], x['road_l'])
    return a
   