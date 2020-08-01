# 5.Eular method
import numpy as np
import math
import matplotlib.pyplot as plt
x,y= [],[]
fx = lambda x,y: x**2+x
x.append(0)
y.append(1)
xn=2
n=20
h = (xn - x[0])/n
for i in range (0,n):
    y.append(y[i]+(h*fx(x[i],y[i])))
    x.append(x[i]+h)
    print(x[i],y[i])
e,f = np.asarray(x),np.asarray(y)
plt.plot(e,f)
plt.show()
