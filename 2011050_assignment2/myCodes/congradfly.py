import numpy as np
import matplotlib.pyplot as plt

# Define parameters
m = 0.2
convergence_criteria = 1e-6
size = 50

# Function to calculate the matrix-vector product
def matvec_product(x):
    Ax = np.zeros_like(x)
    for i in range(size):
        for j in range(size):
            idx = i * size + j
            Ax[idx] = 0.5 * (x[(i+1)%size*size + j] + x[(i-1)%size*size + j] - 2 * x[idx]) + m**2 * x[idx]
    return Ax

# Conjugate Gradient algorithm
def conjugate_gradient(A, b, x0, convergence_criteria, max_iter=1000):
    x = x0
    r = b - A(x)
    p = r
    rsold = np.dot(r, r)
    residuals = [rsold]
    
    for i in range(max_iter):
        Ap = A(p)
        alpha = rsold / np.dot(p, Ap)
        x = x + alpha * p
        r = r - alpha * Ap
        rsnew = np.dot(r, r)
        residuals.append(rsnew)
        if np.sqrt(rsnew) < convergence_criteria:
            break
        p = r + (rsnew / rsold) * p
        rsold = rsnew
    
    return x, residuals

# Initial guess
x0 = np.ones(size**2)

# Generate the right-hand side
b = np.zeros(size**2)
b[size//2] = 1  # Applying periodic boundary condition

# Perform Conjugate Gradient method
inverse, residuals = conjugate_gradient(matvec_product, b, x0, convergence_criteria)

# Plot residue versus iteration steps
plt.plot(residuals)
plt.yscale('log')
plt.xlabel('Iteration Steps')
plt.ylabel('Residue')
plt.title('Residue vs Iteration Steps')
plt.grid(True)
plt.show()
