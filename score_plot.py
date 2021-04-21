# import numpy as np
# from scoreV2 import ScoreV2
# from Iscore import ControlEnum,YTypeEnum
# import plotly.offline as py
# import plotly.graph_objects as go
# np.seterr(invalid='ignore')
# # py.init_notebook_mode(connected=True)

# x= np.arange(0,100,0.001)

# s=ScoreV2("scoreV2 varies:amp","score","used ratio","amp:",3.22*1024)
# data=s.plot([1.05,1.15,1.30,1.37],ControlEnum.amp,x)
# s1=ScoreV2("scoreV2 varies:capacity","score","used ratio","capacity:",YTypeEnum.UsedSize)
# data=s1.plot([128,256,512,1024,2048,3096],ControlEnum.capacity,x)

# import numpy as np
# from score_menglong import ScoreMenglong
# from Iscore import ControlEnum,YTypeEnum
# import plotly.offline as py
# import plotly.graph_objects as go

# # py.init_notebook_mode(connected=True)
# np.seterr(invalid='ignore')
# x= np.arange(0,100,0.1)

# s=ScoreMenglong("scoreV2 varies:amp","score","used ratio","amp:")
# data=s.plot([1.05,1.15,1.30,1.37],ControlEnum.amp,x)
# s1=ScoreMenglong("scoreV2 varies:f","score","used ratio","f:")
# data=s1.plot([20,40,80,100],ControlEnum.f,x)
# s2=ScoreMenglong("scoreV2 varies:capacity","score","used ratio","capacity:",YTypeEnum.UsedSize)
# data=s2.plot([200,500,1000,2000],ControlEnum.capacity,x)


# import numpy as np
# from scoreB import ScoreB
# from Iscore import ControlEnum,YTypeEnum
# import plotly.offline as py
# import plotly.graph_objects as go

# # py.init_notebook_mode(connected=True)
# np.seterr(invalid='ignore')
# x= np.arange(0,100,0.1)

# s=ScoreB("scoreV2 varies:amp","score","used ratio","amp:")
# data=s.plot([1.05,1.15,1.30,1.37],ControlEnum.amp,x)
# s2=ScoreB("scoreV2 varies:capacity","score","used ratio","capacity:",YTypeEnum.UsedSize,3.22*1024)
# data=s2.plot([200,500,1000,2000],ControlEnum.capacity,x)
# s3=ScoreB("scoreB varies:b","score","used szie","b:",YTypeEnum.UsedSize)
# data=s3.plot([1e1,1e3,1e5],ControlEnum.b,x)

import numpy as np
from scoreCoth import ScoreCoth
from Iscore import ControlEnum,YTypeEnum
import plotly.offline as py
import plotly.graph_objects as go

# py.init_notebook_mode(connected=True)
np.seterr(invalid='ignore')
x= np.arange(0,100,0.01)


s2=ScoreCoth("scoreV2 varies:capacity","capacity:",YTypeEnum.UsedSize,3.22*1024)
data=s2.plot([200,500,1000,2000],ControlEnum.capacity,x)
