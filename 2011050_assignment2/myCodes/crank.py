import numpy as np
import myCodes.matmult as mult
import myCodes.gjinverter as gjinv
import matplotlib.pyplot as plt

def main(L,T,Nx,Nt,g):
    # defining spacings on the grid
    dx = L / Nx
    dt = T / Nt

    # Crank-Nicolson parameter
    alpha = dt / (dx**2)

    x_values = np.linspace(0, L, Nx+1)
    t_values = np.linspace(0, T, Nt+1)

    # Initialize solution matrix
    u=[]
    for i in range(Nx+1):
        r=[]
        for j in range(Nt+1):
            r.append(0.0)
        u.append(r)
    u=np.matrix(u)
    #initialize the matrices coming between the calculation
    A=[]
    for i in range(Nx+1):
        r=[]
        for j in range(Nx+1):
            r.append(0.0)
        A.append(r)
    A=np.matrix(A)
    B=[]
    for i in range(Nx+1):
        r=[]
        for j in range(Nx+1):
            r.append(0.0)
        B.append(r)
    B=np.matrix(B)
    D=[]
    for i in range(Nx+1):
        r=[]
        for j in range(1):
            r.append(0.0)
        D.append(r)
    D=np.matrix(D)
    # Crank-Nicolson process
    #forming the matrix after determining the matrix manually using pen and paper
    for i in range (Nx+1):
        for j in range (Nx+1):
            if i==j:
                A[i,j]=1+(4*alpha)
                B[i,j]=1-(4*alpha)
            elif abs(i-j)==1:
                A[i,j]=(-2*alpha)
                B[i,j]=(2*alpha)
            else:
                A[i,j]=0
                B[i,j]=0
    #inverse the matrix using Gauss-Jordan inversion (as the matrix is sparse) and multiply
    Ainv=gjinv.main(A)
    C=mult.main(Ainv,B)
    # Apply initial condition
    for i in range (Nx+1):
        u[i,0]=g(x_values[i])
    for j in range (Nt):
        for i in range (Nx+1):
            D[i]=u[i,j]
        E=mult.main(C,D)
        for i in range (Nx+1):
            u[i,j+1]=E[i]
    # Display the solution table
    print("Solution Table:")
    print(u)

    # Display the solution in a contour plot
    X, T = np.meshgrid(x_values, t_values)
    plt.contourf(X, T, u.T, cmap='plasma')
    plt.colorbar()
    plt.xlabel('x')
    plt.ylabel('t')
    plt.title('Solution of the given Heat Equation (Crank-Nicolson)')
    plt.show()