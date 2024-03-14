import math

def main(f,d,x):
    ct=1
    a=f(x)/d(x)
    while abs(a)> 10**-6:
        a=f(x)/d(x)
        x=x-a
        ct+=1
    print("No. of iterations in newton raphson method:",ct)
    print("The root of the equation using newton raphson method:",round(x,6))

