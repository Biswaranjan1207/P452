import matplotlib.pyplot as plt
import math


def couple1(dzdx,dTdx,z0,y0,x0,xn,dx):
    X=[]
    Y=[]
    Z=[]
    while x0 < xn :
        Z.append(z0)
        Y.append(y0)
        X.append(x0)
        k1z=dx*dzdx(z0,y0,x0)
        k1y=dx*dTdx(z0,y0,x0)
        k2z=dx*dzdx(z0+k1z/2,y0+k1y/2,x0+dx/2)
        k2y=dx*dTdx(z0+k1z/2,y0+k1y/2,x0+dx/2)
        k3z=dx*dzdx(z0+k2z/2,y0+k2y/2,x0+dx/2)
        k3y=dx*dTdx(z0+k2z/2,y0+k2y/2,x0+dx/2)
        k4z=dx*dzdx(z0+k3z,y0+k3y,x0+dx)
        k4y=dx*dTdx(z0+k3z,y0+k3y,x0+dx)
        z0+= (k1z + 2*k2z + 2*k3z + k4z)/6
        y0+= (k1y + 2*k2y + 2*k3y + k4y)/6
        x0+=dx
    plt.plot(X,Y)
    return y0

def couple2(dzdx,dTdx,z0,y0,yn,x0,xn,dx):
    X=[]
    Y=[]
    Z=[]
    while x0 < xn :
        Z.append(z0)
        Y.append(y0)
        X.append(x0)
        k1z=dx*dzdx(z0,y0,x0)
        k1y=dx*dTdx(z0,y0,x0)
        k2z=dx*dzdx(z0+k1z/2,y0+k1y/2,x0+dx/2)
        k2y=dx*dTdx(z0+k1z/2,y0+k1y/2,x0+dx/2)
        k3z=dx*dzdx(z0+k2z/2,y0+k2y/2,x0+dx/2)
        k3y=dx*dTdx(z0+k2z/2,y0+k2y/2,x0+dx/2)
        k4z=dx*dzdx(z0+k3z,y0+k3y,x0+dx)
        k4y=dx*dTdx(z0+k3z,y0+k3y,x0+dx)
        z0+= (k1z + 2*k2z + 2*k3z + k4z)/6
        y0+= (k1y + 2*k2y + 2*k3y + k4y)/6
        x0+=dx
        if abs(y0-yn)<=10**-3:
            return x0-dx