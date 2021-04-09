#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
from Iscore import IScore,ControlEnum

class ScoreV3(IScore):
  
    def score(self,varibleType:ControlEnum,varible,x:np.ndarray):
        np.seterr(invalid='ignore')
        m=256
        capacity=1000

        if varibleType==ControlEnum.capacity:
            capacity=varible
        
        u=x/100*capacity
        a=capacity-u

        return  m*(np.log(capacity)-np.log(a))

