#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
from Iscore import IScore,ControlEnum,YTypeEnum

class ScoreCoth(IScore):
  
    def score(self,varibleType:ControlEnum,varible,x:np.ndarray):
        np.seterr(invalid='ignore')
        k=10
        m=2048
        capacity=self.capacity


        if varibleType==ControlEnum.capacity:
            capacity=varible
        elif varibleType==ControlEnum.m:
            m=varible    

        if(self.YType==YTypeEnum.UsedSize):
            u=x
        else:
            u=x/100*capacity

        u[np.where(u>capacity)]=0    
        
        a=capacity-u

        score=(capacity-a)/m+k*1/np.tanh(a/m)
        

        return  score

