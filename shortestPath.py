from numpy import *
import matplotlib.pyplot as plt


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
    
    
def plotflight(dataset, place):
    weight = []
    height = []
    plt.style.use('fivethirtyeight')        
    plt.title('flight price')    
    for i in range(6):
        weight.append(random.randint(i*(3-i)*15, i*(3-i)*15+5))
        height.append(random.randint((i%2)*15, (i%2)*15+5))
        plt.text(height[i]+1, weight[i]+1, '%d'%(i+1), color='blue')   
        plt.plot(height[i], weight[i], 'ro')             

    for i in range(7):
       
        for j in range(1, i + 1):
            
            if dataset[i-1][j]<100 and dataset[i-1][j]>0:
                plt.text((height[i-1]+height[j-1])/2, (weight[i-1]+weight[j-1])/2, '%d'%dataset[i-1][j], color='black')
                plt.plot([height[i-1], height[j-1]], [weight[i-1], weight[j-1]], color='black', linewidth = 1)                                                                          
    plt.show()

    return weight, height

def fun1(s): return s if s < 100 and s > 0 else None


A = dtype({'names': ['ai', 'tan', 'bn'], 'formats': ['i', 'i' , 'int32']}, align = True)
B = dtype({'names': ['bni'], 'formats': ['i']}, align = True)

def primgraph(dataset, place):
    #the adding struct this turn
    dataset, place = file2matrix('flight_price.txt')
    #plotflight(dataset, place)
    An=[];ai=1
    endpoint = 4 #end point
    
    a = array([(1, 0, 0)], dtype = A)
    print "adding point = a%d ; shortest way to an = %d "%(a[0]['ai'], a[0]['tan'])
    An.append(a[0]['ai'])
    print An
    print "adding the v%d point to An[],marked that the point has been found\n"%a[0]['ai']
    
    
    print "the distence near this point is:"
    print dataset[a[0]['ai']-1][1:]
    #find the point nearby
    Nan_value = filter(lambda x: x < 100 and x > 0, dataset[a[0]['ai']-1][1:])
    print "Nan_value:"
    print Nan_value
    
    Nan_index=[]
    for x in Nan_value:
        if list(dataset[a[0]['ai']-1][1:]).index(x)+1 not in An:
            Nan_index.append(list(dataset[a[0]['ai']-1][1:]).index(x)+1)
    print "Nan_index:"
    print Nan_index
    
    #print dataset[a[0]['ai']-1][1:]
    min_bni = min(Nan_value) 
    vi_index=list(dataset[a[0]['ai']-1][1:]).index(min_bni)+1
    print 'the nearest point is the %d point,the price is: %d $'%(vi_index, min_bni)
    a=vstack((a, array([(vi_index, min_bni , 0)], dtype=A)))
    
    flag=0
    ti = {}
    min_price={}
       
    for i in range(2):
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
        
        print "Nan_value [%d]:"%i 
        print Nan_value
        print "Nan_index [%d]:"%i 
        print Nan_index
        print "the minest point to a%d is v%d "%(i+1,Nan_index[0])
                    
 
    '''
        for x in Nan_value:
            if list(dataset[a[i]['ai']-1][1:]).index(x)+1 not in An:
                Nan_index.append(list(dataset[a[0]['ai']-1][1:]).index(x)+1)
        print "Nan_index [%d]:"%i 
        print Nan_index   
       
    
    bni = array(list(Nan_value),dtype = B)
    print list(Nan_value)
    print "bni"
    print bni[0]['bni']
    
    
    ai_1 = vi_index 
    while ai_1 != endpoint:
        flag=flag+1
        ti["1-%d"%vi_index]=min_bni
     
        print ti
        a=vstack((a, array([(vi_index, min_bni , 0)], dtype=A))) #adding new point's infor        
        
        anow=a[flag]['ai'][0]
        
        print "adding point = a%d ; shortest way from a1 to a%d = %d "%(anow, anow, a[flag]['tan'])
        
        An.append(anow)
        print "An:"
        print An
        print "adding the v%d point to An[],marked that the point has been found\n"%anow
        
        print "the point near this point is:"        
        print dataset[anow-1][1:]

        #find the point nearby
        Nan_value = filter(lambda x: x<100 and x > 0 and list(dataset[anow-1][1:]).index(x)+1 not in An, dataset[anow-1][1:])
        print "Nan_value:";print Nan_value                                                  
        Nan_index=[]
        for x in Nan_value:
            Nan_index.append(list(dataset[anow-1][1:]).index(x)+1)        
        print "Nan_index:";print Nan_index
        min_bni = min(Nan_value)
        vi_index=list(dataset[anow-1][1:]).index(min_bni)+1  
        print 'the nearest point is the %d point,the price is: %d $'%(vi_index, min_bni)      
        ai_1 = vi_index
    '''
