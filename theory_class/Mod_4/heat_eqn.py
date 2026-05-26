import matplotlib.pyplot as plt
import numpy as np

# Parameters
L = 1.0
N = 20
alpha = 0.01

dx = L / N
r = 0.4
dt = r * dx**2 / alpha

# Grid
x = np.linspace(0, L, N + 1)

# Initial condition
u = np.sin(np.pi * x)

# Time stepping
t_final = 0.5
t = 0

while t < t_final:
    u_new = u.copy()

    # Forward-Time Central-Space (FTCS)
    for i in range(1, N):
        u_new[i] = u[i] + r * (u[i + 1] - 2 * u[i] + u[i - 1])

    # Boundary conditions
    u_new[0] = 0
    u_new[N] = 0

    u = u_new
    t += dt

# Plot
plt.title("1D Heat Equation Solution")
plt.xlabel("Position (x)")
plt.ylabel("Temperature")
plt.plot(x, u, label="Temperature at t=0.5")
plt.legend()
plt.grid()
plt.show()
