import numpy as np
import matplotlib.pyplot as plt

L = 0.25          # Length of the fin in meters (25 cm)
N = 10            # Number of spatial divisions
dx = L / N        # Step size (delta x)
h = 100.0         # Convective heat transfer coefficient (W/m^2 K)
k = 175.0         # Thermal conductivity (W/m K)
P = 0.20          # Perimeter = 4 * 0.05m = 0.20 m
A = 0.0025        # Cross-sectional area = 0.05m * 0.05m = 0.0025 m^2
m = np.sqrt((h * P) / (k * A))
coeff = 2 + (m**2 * dx**2)

mat_A = np.zeros((N+1, N+1))
vec_R = np.zeros(N+1)

# Boundary Condition 1: Base temperature (Node 0)
mat_A[0, 0] = 1.0
vec_R[0] = 1.0

# Internal Nodes (Nodes 1 to N-1)
for i in range(1, N):
    mat_A[i, i-1] = 1.0
    mat_A[i, i]   = -coeff
    mat_A[i, i+1] = 1.0
    vec_R[i]      = 0.0

# Boundary Condition 2: Insulated tip (Node N)
mat_A[N, N-1] = 2.0
mat_A[N, N]   = -coeff
vec_R[N]      = 0.0

Theta_numerical = np.linalg.solve(mat_A, vec_R)

x_vals = np.linspace(0, L, N+1)
Theta_analytical = np.cosh(m * (L - x_vals)) / np.cosh(m * L)

print(f"{'x (m)':<10} | {'Theta (Numerical)':<20} | {'Theta (Analytical)'}")
print("-" * 55)
for x, t_num, t_ana in zip(x_vals, Theta_numerical, Theta_analytical):
    print(f"{x:<10.3f} | {t_num:<20.6f} | {t_ana:.6f}")

plt.figure(figsize=(9, 6))

plt.plot(x_vals, Theta_numerical, marker='o', linestyle='-', color='blue', label='Numerical (Finite Difference)', markerfacecolor='white', markeredgecolor='black', markersize=8, markeredgewidth=1)
plt.plot(x_vals, Theta_analytical, marker='s', linestyle='--', color='red', label='Analytical Solution', markerfacecolor='none', markeredgecolor='black', markersize=12, markeredgewidth=1)

plt.title('Temperature Distribution in an Insulated Tip Fin',  fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Distance from Base, x (m)', fontsize=12)
plt.ylabel('Dimensionless Temperature, $Theta$', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()
