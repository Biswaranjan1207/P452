import numpy as np
import matplotlib.pyplot as plt

def leapfrog(f, y0, v0, t0, T, h):
    # Number of time steps
    num_steps = int((T - t0) / h)

    # Initialize arrays to store results
    t_values = np.linspace(t0, T, num_steps + 1)
    y_values = np.zeros_like(t_values)
    v_values = np.zeros_like(t_values)
    
    # Set initial conditions
    y_values[0] = y0
    v_values[0] = v0

    # Leapfrog algorithm
    for i in range(num_steps):
        t_n = t_values[i]
        y_n = y_values[i]
        v_n = v_values[i]

        # Update velocity at the half-step
        v_half = v_n + 0.5 * h * f(t_n, y_n)

        # Update position and velocity
        y_values[i + 1] = y_n + h * v_half
        v_values[i + 1] = v_half + 0.5 * h * f(t_n + h, y_values[i + 1])

    return t_values, y_values

# Example: Solve the simple harmonic oscillator ODE dy/dt = v, dv/dt = -y
def f(t, y):
    return -y

# Initial conditions and time parameters
y0 = 1.0
v0 = 0.0
t0 = 0.0
T = 10.0
h = 0.1

# Solve the ODE using leapfrog algorithm
t_values, y_values = leapfrog(f, y0, v0, t0, T, h)

# Plot the results
plt.plot(t_values, y_values, label='Leapfrog')
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.legend()
plt.show()
