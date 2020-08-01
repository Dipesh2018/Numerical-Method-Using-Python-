# 3. Trapezoidal rule
import numpy as np
fx = lambda x : np.sin(x)/np.exp(x)
x,y = [],[]
x.append(0)
xn= np.pi
n=20
h,value =(xn - x[0])/n,0
for i in range (0,n):
    x.append(x[0]+i*h)
    y.append(fx(x[i]))
    if (i!=0 or i!=n):
        value = value + y[i]
final_ans = (h/2)*(y[0]+y[n-1]+2*value)
print (final_ans,"is the final answer")
