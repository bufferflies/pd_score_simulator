import math

class WMA:
    # size=0
    # records=[]
    # count=0
    def __init__(self,size):
        self.size=int(size)
        self.records=[]
        self.count=0
    def Add(self,n):
        if self.count<self.size:
            self.records.append(n)
        else:
           self.records[self.count%self.size]=n    
        self.count=self.count+1  
    def Get(self):
        if self.count==0:
            return 0
        sum=0
        if self.count<self.size:
            for i in range (0,self.count):
                 sum=sum+self.records[i]    
            return sum/self.count
        for i in range (0,self.size):
            sum=sum+self.records[(self.count+i)%self.size]*(i+1)
        count= (self.size+1)*self.size/2
        return sum/count

    def Reset(self):
        self.count=0

    def Set(self,n):
        self.Reset()
        self.Add(n)

class HMA:
    # size=0
    # wma=[]
    def __init__(self,size):
        self.size=size
        self.wma=[]
        self.wma.append(WMA(self.size/2))
        self.wma.append(WMA(self.size))
        self.wma.append(WMA(math.sqrt(self.size)))

    def Add(self,n):
        self.wma[0].Add(float(n))  
        self.wma[1].Add(float(n))  
        self.wma[2].Add(2*self.wma[0].Get()-self.wma[1].Get())  
    def Get(self):
        return self.wma[2].Get()
    def Reset(self):
        self.wma.append(WMA(self.size/2))
        self.wma.append(WMA(self.size))
        self.wma.append(WMA(math.sqrt(self.size))) 
    def Set(self,n):
        self.Reset()
        self.Add(n)       
