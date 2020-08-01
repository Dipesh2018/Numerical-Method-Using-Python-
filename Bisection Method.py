import numpy as np 
import matplotlib.pyplot as plt 
import math
fx = lambda x : x**2 - np.sin(x)
a,b,n,i = 0.5,1,1,1
print ("Iteration \t a\tb")
while (n == 1):
    x1,x2=fx(a),fx(b)
    print (i ,'\t\t', a, '\t', b)
    i = i + 1
    if (x1*x2 < 0):
        mid_value = (a + b) / 2
        x3 = fx(mid_value)
        if (x3 == 0):print(mid_value," is the root.")
        elif (x1 * x3 < 0):b = mid_value
        elif (x2 * x3 < 0):a = mid_value
    if (b-a<0.001):
        print(mid_value,"the root is")
        break
