#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
from Iscore import IScore,ControlEnum,YTypeEnum

class ScoreV3(IScore):
  
    def score(self,varibleType:ControlEnum,varible,x:np.ndarray):
        np.seterr(invalid='ignore')
        m=256
        capacity=1000
        k=1
        amp=1.05

        if varibleType==ControlEnum.capacity:
            capacity=varible
        if(self.YType==YTypeEnum.UsedSize):
            u=x
        else:
            u=x/100*capacity
        # u=x/100*capacity
        a=capacity-u

        return  k*amp*u+m*(np.log(capacity)-np.log(a))
