#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
from Iscore import IScore
class Score(IScore):
    # k: control variable
    # x: used ratio 
    def score(self,k,x:np.ndarray):
        u=x/100*self.capacity
        return  u/self.capacity
