import numpy as np  
#calculating the legendre polynomials upto nth order
def legendre_polynomial(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return ((2 * n - 1) * x * legendre_polynomial(n - 1, x) - (n - 1) * legendre_polynomial(n - 2, x)) / n

#calculating the roots of the legendre polynomials and forming arrays for different orders
def legendre_roots(n):
    # Initial approximation of roots using Chebyshev nodes
    x = np.cos(np.pi * (4 * np.arange(1, n + 1) - 1) / (4 * n + 2))
    # Improved approximation using Newton's method
    for i in range(5):  # Iterate for refinement (adjust the number of iterations as needed)
        x -= legendre_polynomial(n, x) / legendre_polynomial_derivative(n, x)

    return x
#calculating the derivative of the legendre polynomials upto nth order
def legendre_polynomial_derivative(n, x):
    return n / (x**2 - 1) * (x * legendre_polynomial(n, x) - legendre_polynomial(n - 1, x))
#main function implementing the gaussian quadrature
def gqi(f,a, b, num_points):
    # Compute Legendre roots and weights
    roots = legendre_roots(num_points)
    weights = 2 / ((1 - roots**2) * legendre_polynomial_derivative(num_points, roots)**2)

    # Map the roots to the interval [a, b]
    mapped_roots = 0.5 * (b - a) * roots + 0.5 * (a + b)

    # Perform the Gaussian quadrature integration
    result = np.sum(weights * f(mapped_roots))
    return 0.5 * (b - a) * result



