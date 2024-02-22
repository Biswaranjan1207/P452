import numpy as np
import matplotlib.pyplot as plt

def main(L,T,Nx,Nt,g):
    # Grid spacings
    dx = L / (Nx - 1)
    dt = T / Nt

    # Crank-Nicolson parameter
    alpha = dt / (2 * dx**2)


    # Set up grid
    x_values = np.linspace(0, L, Nx)
    t_values = np.linspace(0, T, Nt)

    # Initialize solution matrix
    u = np.zeros((Nx, Nt))

    # Apply initial condition
    u[:, 0] = g(x_values)

    # Crank-Nicolson time-stepping scheme
    for j in range(0, Nt - 1):
        A = np.diag(-alpha * np.ones(Nx - 1), k=-1) + np.diag((2 + 2 * alpha) * np.ones(Nx)) + np.diag(-alpha * np.ones(Nx - 1), k=1)
        B = np.diag(alpha * np.ones(Nx - 1), k=-1) + np.diag((2 - 2 * alpha) * np.ones(Nx)) + np.diag(alpha * np.ones(Nx - 1), k=1)
        
        u[:, j + 1] = np.linalg.solve(A, np.dot(B, u[:, j]))

    # Display the solution in a table
    print("Solution Table:")
    print(u)

    # Display the solution in a contour plot
    X, T = np.meshgrid(x_values, t_values)
    plt.contourf(X, T, u.T, cmap='viridis')
    plt.colorbar()
    plt.xlabel('x')
    plt.ylabel('t')
    plt.title('Solution of the Heat Equation (Crank-Nicolson)')
    plt.show()
