from hma import HMA,WMA
data=[120, 130, 140, 150, 145, 136, 121, 132, 145, 156, 148, 157, 175]

h=HMA(5)
w=WMA(5)
e=[]
e1=[]
for i in range(len(data)):
    h.Add(data[i])
    w.Add(data[i])
    e.append(h.Get())
    e1.append(w.Get())

print(e)    
print(e1)