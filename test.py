import numpy as np
A=np.array([[1,1,0,1],[1,0,1,1],[0,1,1,1],[1,1,1,0]])
S=np.diag((25,30,40,50))
Amp=np.diag((1.1,1.2,1.3,1.4))
Store=np.dot(S,A)
Size=np.dot(Store,Amp)
Size