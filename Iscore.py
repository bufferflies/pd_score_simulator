#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
from abc import ABCMeta, abstractmethod
from enum import Enum,unique
import plotly.graph_objects as go

@unique
class ControlEnum(Enum):
    capacity=0
    f=1
    amp=2
    m=3
    b=4

@unique
class YTypeEnum(Enum):
    UsedSize=0
    UsedRatio=1

class IScore(metaclass=ABCMeta):

    title=''
    xlabel=''
    ylabel=''
    
    capacity=1
    legend='k'
    capacity=1000

    
    YType=YTypeEnum.UsedRatio

    def __init__(self,title,legend,yType=YTypeEnum.UsedRatio,capacity=1000):
        self.title=title
        self.xlabel="score"
        self.legend=legend
        self.YType=yType
        self.capacity=capacity
        if yType==YTypeEnum.UsedRatio:
            self.ylabel="used ratio"
        else:
            self.ylabel="used size"
            

    # k: control variable
    # x: used ratio 
    @abstractmethod
    def score(self,control,k,x:np.ndarray):
        u=x/100*self.capacity
        return  u+k*(np.log(self.capacity)-np.log(self.capacity-u))

    def plot(self,ks,control:ControlEnum,x:np.ndarray):
        arr=[]
        layout=go.Layout(title=self.title,xaxis={'title':self.xlabel},yaxis={'title':self.ylabel})
        y=x
        if self.YType==YTypeEnum.UsedSize:
            if control==ControlEnum.capacity:
                y=np.max(ks)*x/100
            else:
                y=self.capacity*x/100

        for i in ks:
            arr.append(go.Scatter(name=self.legend+str(i),x=self.score(control,i,np.copy(y)),y=y))

        fig=go.Figure(data=arr,layout=layout)
        fig.show()
       
      