import math 
fx = lambda x : math.exp(x) - 4*x
deriv = lambda x : math.exp(x) -4
x0,i,n = 1.0,1,1
while (n == 1):
    i = i+1
    x1 = x0 - (fx(x0) / deriv(x0))
    print (i,"\t",x0)
    if (abs(x1 - x0) < 0.00001 ):
        print("The root is ",x1)
        break
    else:
        x0 = x1
