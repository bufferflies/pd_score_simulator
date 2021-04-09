#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import plotly.graph_objects as go
from abc import ABCMeta, abstractmethod
from enum import Enum,unique
import plotly.graph_objects as go

@unique
class ControlEnum(Enum):
    capacity=0
    f=1
    amp=2


class IScore(metaclass=ABCMeta):

    title=''
    xlabel=''
    ylabel=''
    
    capacity=1
    legend='k'
    

    def __init__(self,title,xlabel,ylabel,legend):
        self.title=title
        self.xlabel=xlabel
        self.ylabel=ylabel
        self.legend=legend

    # k: control variable
    # x: used ratio 
    @abstractmethod
    def score(self,control,k,x:np.ndarray):
        u=x/100*self.capacity
        return  u+k*(np.log(self.capacity)-np.log(self.capacity-u))

    def plot(self,ks,control:ControlEnum,x:np.ndarray):
        arr=[]
        layout=go.Layout(title=self.title,xaxis={'title':self.xlabel},yaxis={'title':self.ylabel})
        for i in ks:
            arr.append(go.Scatter(name=self.legend+str(i),x=self.score(control,i,x),y=x))
            # ax.plot(self.score(i,x),x,label=self.legend+str(i))        s=ScoreV2("scoreV2 varies:amp","score","used","amp:")

        fig=go.Figure(data=arr,layout=layout)
        fig.show()
       
      