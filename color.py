#导入模块
import plotly.graph_objects as go
import numpy as np

class Storage:
    title=''
    xlabe=[]
    ylable=[]
    def __init__(self,title,regionIds,storeIds):
        self.title=title
        self.xlabe=regionIds
        self.ylable=storeIds

    # location is NXM(N: regions M: store) 0-1 metrix
    # approximateSize: diag(approximateSize) metrix 
    # amp: diag(amp) metrix  
    def Plot(self,location,approximateSize,amp):
        Size=np.diag(approximateSize)
        Amp=np.diag(amp)
        LogicalStore=np.dot(Size,location)
        PhysicalStore=np.dot(LogicalStore,Amp)
        z=PhysicalStore
        fig = go.Figure(data=go.Heatmap(
                        z=z,
                        x=regions,
                        y=stores,
                        hoverongaps = False))
        fig.show()
regions=['1','2','3','4']
stores=['1','2','3','4']

s=Storage("storage visual",regions,stores)
location=np.array([[1,1,0,1],[1,0,1,1],[0,1,1,1],[1,1,1,0]])
approximateSize=(25,30,40,50)
Amp=(1.1,1.2,1.3,1.4)
s.Plot(location,approximateSize,Amp)

