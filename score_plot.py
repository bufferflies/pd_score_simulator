import numpy as np
from scoreV2 import ScoreV2
from Iscore import ControlEnum

import plotly.graph_objects as go

x= np.arange(80,100,0.1)

s=ScoreV2("scoreV2 varies:amp","score","used ratio","amp:")
data=s.plot([1.05,1.15,1.30,1.37],ControlEnum.amp,x)
