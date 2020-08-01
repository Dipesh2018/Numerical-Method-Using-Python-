# 6.R-K Method
import numpy as np
import matplotlib.pyplot as plt 
fx = lambda x,y : x**2 + x
x,y = [], []
x.append(0)
y.append(1)
n=10
xn=2
h =(xn-x[0])/n
for i in range (0,n):
    k1 = h * fx(x[i],y[i])
    k2 = h * fx(x[i]+h,y[i]+k1)
    y.append(y[i]+(1/2)*(k1+k2))
    x.append(x[i]+h)
    print(y[i],x[i])
x,y= np.asarray(x),np.asarray(y)
plt.plot(x,y)
plt.show()
