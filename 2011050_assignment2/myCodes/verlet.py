def pos(x0,v0,a,tn,dt):
    x1 = x0 + (v0*dt) + (a(x0)*dt*dt/2)
    xnm1 = float(x0)
    xn = float(x1)
    for i in range (1,tn/dt):
        xnp1 = (2*xn) - xnm1 + (a(xn)*dt*dt)
        xnm1 = float(xn)
        xn = float(xnp1)
    return xn

def vel(x0,v0,a,tn,dt):
    xn = float(x0)
    vn = float(v0)
    for i in range (0,tn/dt):
        vthdt = xn + (vn*dt) + (a(xn)*dt/2)
        xnp1 = xn + (vthdt*dt)
        vnp1 = vn + ((a(xn)+a(xnp1))/2)
        vn = float(vnp1)
        xn = float(xnp1)
    return vn

# Constants
m = 1.0  # Mass
k = 10.0  # Spring constant
dt = 0.01  # Time step
total_steps = 1000  # Total number of steps

# Initial conditions
x = 1.0  # Initial position
v = 0.0  # Initial velocity

# Verlet integration
for step in range(total_steps):
    # Calculate acceleration using the force equation (F = -kx)
    a = -k * x / m
    
    # Update position using Verlet integration
    x_new = x + v * dt + 0.5 * a * dt**2
    
    # Update velocity using Verlet integration
    v = v + 0.5 * (a + (-k * x_new / m)) * dt
    
    # Update position for the next iteration
    x = x_new
    
    # Print results (optional)
    print(f"Step {step + 1}: Time = {dt * (step + 1):.2f}, Position = {x:.4f}, Velocity = {v:.4f}")
