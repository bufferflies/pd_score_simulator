from  matplotlib import pyplot as plt
import numpy as np
from score import Score
from scoreV2 import ScoreV2


x= np.arange(50,90,0.01)
plt.figure(1)

# generate 1 row 2 col picture 
ax1=plt.subplot(221)
s=Score(100,"u/c","score","used","k")
s.plot(ax1,[100,500,1000,2000],x)

ax2=plt.subplot(222)

s=ScoreV2(3.22*1024,"scoreV2","score","used","amp")
s.plot(ax2,[1.05,1.15,1.30,1.37],x)

plt.show()