import math
import matplotlib.pyplot as plt
def partial(Lx,Nx,Lt,Nt):
    hx=Lx/Nx
    ht=Lt/Nt
    alpha=ht/(hx**2)
    V0=[0]*(Nx+1)
    V1=[0]*(Nx+1)
    I=[]
    print("The value of alpha is:", round(alpha,5))
    if alpha<0.5:
        print("The condition of alpha << 0.5 is satisfied...")
    if alpha>0.5:
        print("Beware of the instability!!!!")
    for i in range(0,Nx+1):
        V0[i]=0.0
        I.append(hx*i)
    V0[int(Nx/2)]=573#at centre, temperature is 300 C at t=0
    plt.plot(I,V0)
    for j in range(1,1001):
        for i in range(0,Nx+1):
            if i == 0:
                V1[i]=(1-2*alpha)*V0[i]+alpha*V0[i+1]
            elif i==Nx:
                V1[i]=alpha*V0[i-1]+(1-2*alpha)*V0[i]
            else:
                V1[i]=alpha*V0[i-1]+(1-2*alpha)*V0[i]+alpha*V0[i+1]
        for k in range(0,Nx+1):
            V0[k]=V1[k]
        if j==0: 
            plt.plot(I,V0,label='initial parameter')
        if j==20: 
            plt.plot(I,V0,label='after time=20 units')
        if j==50: 
            plt.plot(I,V0,label='after time=50 units')
        if j==100: 
            plt.plot(I,V0,label='after time=100 units')
        if j==200: 
            plt.plot(I,V0,label='after time=200 units')
        if j==300: 
            plt.plot(I,V0,label='after time=300 units')
    plt.xlabel("Position(x)")
    plt.ylabel("Temperature (Kelvin)")
    plt.legend()
    plt.title("Solution to 1-d heat equation")
    plt.show()
    