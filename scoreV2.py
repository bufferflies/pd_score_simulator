#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
from Iscore import IScore

class ScoreV2(IScore):
    def score(self,k,x:np.ndarray):
        u=x/100*self.capacity
        return  u+k*(np.log(self.capacity)-np.log(self.capacity-u))

