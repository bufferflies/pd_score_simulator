from  matplotlib import pyplot as plt
import numpy as np
from score import Score
from scoreV2 import ScoreV2


x= np.arange(1,100,0.1)
plt.figure(1)

# generate 1 row 2 col picture 
ax1=plt.subplot(121)
s=Score(100,"u/k, k:[100,500,1000,2000]","used","score")
s.plot(ax1,[100,500,1000,2000],x)

ax2=plt.subplot(122)
s=ScoreV2(100,"u+k(log(c)-log(c-u)),k:[100,500,1000,2000]","used","score")
s.plot(ax2,[100,500,1000,2000],x)

plt.show()