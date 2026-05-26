import numpy as np
import matplotlib.pyplot as plt

# Given Parameters
h = 0.2
V = 2
mu = 0.04
N = 101

# Distance array from center to wall
y = np.linspace(-h, h, N)

# Velocity distribution
u = (3 * V / 2) * (1 - (y / h)**2)

# Calculate velocity gradient and shear stress
du_dy = np.gradient(u, y)
tau = mu * du_dy

# Alternatively using the analytical derivative
# tau_analytical = mu * (-3 * V * y) / (h**2)

# Print specific values
tau_bottom = tau[0]
tau_mid = tau[N // 2]
print(f"Shear stress on the bottom wall is {tau_bottom:.4f}")
print(f"Shear stress at mid plane is {tau_mid:.4f}")

# Plotting
plt.figure(figsize=(10, 6))
plt.title("Velocity and Stress Distribution")
plt.xlabel("Velocity and Shear Stress")
plt.ylabel("Position (y)")
plt.plot(u, y, label="Velocity (u)")
plt.plot(tau, y, label="Shear Stress (tau)")
plt.grid()
plt.legend()
plt.show()
