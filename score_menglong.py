#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
from Iscore import IScore,ControlEnum,YTypeEnum

class ScoreMenglong(IScore):
  
    def score(self,varibleType:ControlEnum,varible,x:np.ndarray):
        np.seterr(invalid='ignore')
        k=1
        m=256
        f=20
        capacity=self.capacity
        amp=1.05

        if varibleType==ControlEnum.capacity:
            capacity=varible
        elif varibleType==ControlEnum.amp:
            amp=varible
        elif  varibleType==ControlEnum.f:
            f=varible  
       

        if(self.YType==YTypeEnum.UsedSize):
            u=x
        else:
            u=x/100*capacity

        u[np.where(u>capacity)]=0
        a=capacity-u
        r=u*amp

        # if a>f use score2  else use score1 
        A=np.ones(len(u))
        A[np.where(a<f)]=0
        
        # Piecewise function use A
        score1=A*(k*amp*u+m*(np.log(capacity)-np.log(a-f+1))/(capacity-a+f-1)*r)
        score1[np.argwhere(np.isnan(score1))]=0
        #(K + M*math.Log(C)/(C)) * (R + (F-A)*(C/F))
        score2=(1-A)*((k+m*np.log(capacity)/capacity)*(r+ (f-a)*(capacity/f)))
        return  score1+score2

