import matplotlib.pyplot as plt
import math
def feuler(x0,y0,xn,h,f):
    X=[]
    Y=[]
    ct=1
    while x0 < xn :
        X.append(x0)
        Y.append(y0)
        y0+= h*f(x0,y0)
        x0+= h
        ct+=1
    print(y0)
    plt.scatter(X,Y)
    plt.show()


def beuler(x0,y0,xn,h,f1):
    X=[]
    Y=[]
    ct=1   
    y1=float(y0)
    while x0 < xn :
        X.append(x0)
        Y.append(y0)
        y1=f1(x0+h,y1)
        y0= f1(x0+h,y0)
        x0+= h
    print(y0)
    plt.scatter(X,Y)
    plt.show()

def semi_implicit(x0,v0,t0,tn,dt,f,g):
    xn = float(x0)
    vn = float(v0)
    for i in range (0,tn/dt):
        vnp1 = vn + (g((t0+(dt*i)),xn)*dt)
        xnp1 = xn + (f((t0+(dt*i)),vnp1)*dt)
        vn = float(vnp1)
        xn = float(xnp1)
    return xn,vn

def f1(x,y):
    return y+(h*(math.sin(x)+x**2))
def f2(x,y):
    return (math.sin(x)+x**2)
x0=0
y0=-1
xn=1
h=0.01
beuler(x0,y0,xn,h,f1)
feuler(x0,y0,xn,h,f2)