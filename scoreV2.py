#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
from Iscore import IScore

class ScoreV2(IScore):
  
    def score(self,amp,x:np.ndarray):
        k=1
        m=256
        f=20

        u=x/100*self.capacity
        a=self.capacity-u
        r=u*amp

        # score=k*r+m*(np.log(self.capacity)-np.log(a-f+1)/(u+f-1))*r
        score=k*amp*u+m*(np.log(self.capacity)-np.log(a-f+1))/(self.capacity-a+f-1)*r
        return  score

