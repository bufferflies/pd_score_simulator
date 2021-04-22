
class MaxFilter:
    records=[]
    size=0
    count=0
    
    def __init__(self,size):
        self.size=size

    def Add(self,n):
        if self.count<self.size:
            self.records.append(n)
        else:
            self.records[self.count%self.size]=n
        self.count=self.count+1

    def Get(self):
        return max(self.records)

    def Reset(self):
        self.count=0

    def Set(self,n):
        self.records[0]=n
        self.count=1    


