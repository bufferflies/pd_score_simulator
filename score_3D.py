# plot contour picture about score 
from  matplotlib import pyplot as plt
import numpy as np

# initial  u score 
U=np.arange(1,100,0.1)
C=np.arange(1,100,1)

# UXC： generator shape(UXC)=1000X100
X,Y=np.meshgrid(C,U)
# filter U>C area  
i=0
for x in C:
    Y[x*10:,i]=0
    i=i+1 

# score computor
def f(c,u,k):
    return u+k*(np.log(c)-np.log(c-u-0.01))
def a(c,u):
    return np.divide(u,c)    

def pd(c,u):
    A=u*(1+256*(np.log(c)-np.log(c-u))/(u+0.001))
    return A    

## plot
plt.figure(1)
ax1=plt.subplot(221)
## contour 等高图
P=plt.contour(C,U,f(X,Y,100))
## add contour line label
plt.clabel(P,inline=True)
ax1.set_title("u+k(ln(c)-ln(c-u)),k=100")
plt.xlabel("capacity")
plt.ylabel("used")

ax4=plt.subplot(222)
P=plt.contour(C,U,f(X,Y,10))
ax4.set_title("u+k(ln(c)-ln(c-u)),k=10")
plt.clabel(P,inline=True)

ax3=plt.subplot(223)
P=plt.contour(C,U,f(X,Y,1))
ax3.set_title("u+k(ln(c)-ln(c-u)),k=1")
plt.clabel(P,inline=True)



ax2=plt.subplot(224)
P=plt.contour(C,U,pd(X,Y))
ax2.set_title("u*(1+256*(lnc-lnu)/u)")
plt.clabel(P,inline=True)


plt.show()