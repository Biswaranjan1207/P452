import math
def f(x):
    return x**2-4
  
def bisection(a,b):
 
    if (f(a) * f(b) > 0):
        print("You have not assumed right a and b\n")
        return
    ct=1
    condition = True
    while condition:
 
        # Find middle point
        c = (a+b)/2
  
        # Decide the side to repeat the steps
        if (f(c)*f(a) < 0):
            b = c
        else:
            a = c
        ct+=1
        condition = abs(f(c))>10**-6
    print('No. of iterations for bisection method:',ct)    
    print("The value of root using bisection method is : ",c)
bisection(1,3)
