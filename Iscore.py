#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
from abc import ABCMeta, abstractmethod

class IScore(metaclass=ABCMeta):

    title=''
    xlabel=''
    ylabel=''
    
    capacity=1
    legend='k'
    

    def __init__(self,capacity,title,xlabel,ylabel,legend):
        self.title=title
        self.capacity=capacity
        self.xlabel=xlabel
        self.ylabel=ylabel
        self.legend=legend

    # k: control variable
    # x: used ratio 
    @abstractmethod
    def score(self,k,x:np.ndarray):
        u=x/100*self.capacity
        return  u+k*(np.log(self.capacity)-np.log(self.capacity-u))

    def plot(self,ax,ks,x:np.ndarray):
        for i in ks:
            ax.plot(self.score(i,x),x,label=self.legend+str(i))

        ax.set_xlabel(self.xlabel)
        ax.set_ylabel(self.ylabel)
        ax.set_title(self.title)
        ax.grid()
        ax.legend()
       
      