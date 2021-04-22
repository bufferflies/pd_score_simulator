import plotly.graph_objects as go
import numpy as np

from hma import HMA,WMA
from max_filter import MaxFilter
from request import Prometheus


gb=1024*1024*1024
start="2021-04-19T05:26:30.781Z"
end="2021-04-19T08:57:30.781Z"

p=Prometheus("172.16.4.3",start,end,"33401")
query="pd_scheduler_store_status{type='store_available_deviation',store='1'}"

deviation=p.GetRecords(query)[0].get("values")

query="pd_scheduler_store_status{type='store_available_avg',store='1'}"
avg=p.GetRecords(query)[0].get("values")

pd=[]
x=[]
for i in range(len(avg)):
    pd.append((float(deviation[i][1])+float(avg[i][1]))/gb)
    x.append(i)

query="pd_scheduler_store_status{type='store_available',store='1'}"
available=p.GetRecords(query)[0].get("values")

avgAvailable=HMA(240)
avgMaxAvailableDeviation=HMA(60)
filter=MaxFilter(120)
h=[]
w1=[]
w2=[]

for i in range(len(available)):
    a=float(available[i][1])/gb
    avgAvailable.Add(a)
    d=abs(a-avgAvailable.Get())
    filter.Add(d)
    avgMaxAvailableDeviation.Add(filter.Get())

    w1.append(avgAvailable.Get())
    w2.append(avgMaxAvailableDeviation.Get())

    h.append(avgAvailable.Get()+avgMaxAvailableDeviation.Get())
# print(h)

arr=[]
layout=go.Layout(title='hma',xaxis={'title':'time'},yaxis={'title':'available'})

available=np.array(available)

y=available[:,1].astype(np.float)/(gb)

arr.append(go.Scatter(name='origin',x=x,y=y))
arr.append(go.Scatter(name='pd',x=x,y=pd))
arr.append(go.Scatter(name='py',x=x,y=h))
arr.append(go.Scatter(name='avgAvailable',x=x,y=w1))
fig=go.Figure(data=arr,layout=layout)
fig.show()

