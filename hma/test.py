import plotly.graph_objects as go
import numpy as np

arr=[]
x=np.arange(1,100)
layout=go.Layout(title='hma',xaxis={'title':'time'},yaxis={'title':'available'})
arr.append(go.Scatter(name='origin',x=x,y=np.sin(x)))
# arr.append(go.Scatter(name='pd',x=x,y=pd))
# arr.append(go.Scatter(name='py',x=x,y=h))
fig=go.Figure(data=arr,layout=layout)
fig.show()