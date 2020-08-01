# Simpson 1/3 Method 
import matplotlib.pyplot as plt
import numpy as np
import math
f = lambda x: np.sqrt(1/(2*np.pi))*np.exp(-(x**2)/2)
x = np.linspace(-4,4,50)
y = f(x)
h=x[1]-x[0]
sum=0
for i in range(1,49,2):
    sum=sum+y[i]
sum1=0
for i in range(2,48,2):
    sum1=sum1+y[i]

I=(h/3)*(y[0]+y[49]+4*sum+2*sum1)
print("The final value is","%.2f"% I)
plt.plot(x,y)
plt.show()
