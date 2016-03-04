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
                    
    #plt.scatter(height, weight)
    
    for i in range(7):
       
        for j in range(1, i + 1):
            
            if dataset[i-1][j]<100 and dataset[i-1][j]>0:
                plt.text((height[i-1]+height[j-1])/2, (weight[i-1]+weight[j-1])/2, '%d'%dataset[i-1][j], color='black')
                plt.plot([height[i-1], height[j-1]], [weight[i-1], weight[j-1]], color='black', linewidth = 1)                
                               
        #plt.plot(height[i], weight[i], 'r')
                                                                       
    plt.show()
    #plt.clf()
   
    return weight, height


A = dtype({'names': ['ai', 'tan',  'Ti', 'bn'], 'formats': ['i', 'i' , 'S10', 'int32']}, align = True)

def primgraph(dataset,place):
    #the adding struct this turn
    dataset, place = file2matrix('flight_price.txt')
    plotflight(dataset, place)
    An=[]
    a = array([(1, 0, "", 0)], dtype = A)
    print "adding point = a%d ; shortest way to an = %d ; collection of shortest way = %s"%(a[0]['ai'], a[0]['tan'], a[0]['Ti'])
    An.append(a[0]['ai'])
    print "adding the v%d point to An[],marked that the point has been found\n"%a[0]['ai']
    
    
    print "the distence near this point is:"
    print dataset[a[0]['ai']-1][1:]
    #find the point nearby
    Nan_value = filter(lambda x: x<100 and x > 0, dataset[a[0]['ai']-1][1:])
    print "Nan_value:"
    print Nan_value
    
    Nan_index=[]
    for x in Nan_value:
        if list(dataset[a[0]['ai']-1][1:]).index(x)+1 not in An:
            Nan_index.append(list(dataset[a[0]['ai']-1][1:]).index(x)+1)
        #Nan_index.append(list(dataset[a[0]['ai']-1][1:]).index(x))
    print "Nan_index:"
    print Nan_index
    
    #sort the distance to find ai's nearest
    #b=sort(dataset[a[0]['ai']-1][1:])
    
    #sort(list(b))
    print dataset[a[0]['ai']-1][1:]
    bni = min(Nan_value)
    
    print bni
    vi_index=list(dataset[a[0]['ai']-1][1:]).index(bni)+1
    print 'the nearest point is the %d point,the price is: %d $'%(vi_index, bni)
    b = 4
    flag=0
    while b != ai:
        flag=flag+1
        a.append(array([(vi_index, bni, "", 0)]))
        print "adding point = a%d ; shortest way to an = %d ; collection of shortest way = %s"%(a[flag]['ai'], a[flag]['tan'], a[flag]['Ti'])
        An.append(a[0]['ai'])
        print "adding the v%d point to An[],marked that the point has been found\n"%a[0]['ai']
            
            
            print "the distence near this point is:"
            print dataset[a[0]['ai']-1][1:]
            #find the point nearby
            Nan_value = filter(lambda x: x<100 and x > 0, dataset[a[0]['ai']-1][1:])
            print "Nan_value:"
            print Nan_value
            
            Nan_index=[]
            for x in Nan_value:
                if list(dataset[a[0]['ai']-1][1:]).index(x)+1 not in An:
                    Nan_index.append(list(dataset[a[0]['ai']-1][1:]).index(x)+1)
                #Nan_index.append(list(dataset[a[0]['ai']-1][1:]).index(x))
            print "Nan_index:"
            print Nan_index
            
            #sort the distance to find ai's nearest
            #b=sort(dataset[a[0]['ai']-1][1:])
            
            #sort(list(b))
            print dataset[a[0]['ai']-1][1:]
            b = min(Nan_value)
            
            print b
            vi_index=list(dataset[a[0]['ai']-1][1:]).index(b)+1        

    
