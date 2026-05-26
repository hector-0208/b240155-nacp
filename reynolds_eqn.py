import matplotlib.pyplot as plt
import numpy as np

epsilon = 0.9  # Eccentricity ratio
L_D = 0.5  # L/D ratio
D_L = 1.0 / L_D
M = 88  # Number of nodes in theta direction
N = 22  # Number of nodes in z direction
theta_0, theta_n = 0.0, 2.0 * np.pi
z_0, z_n = 0.0, 1.0

d_theta = (theta_n - theta_0) / (M - 1)
dz = (z_n - z_0) / (N - 1)

theta = np.linspace(theta_0, theta_n, M)

C = (1 / 4) * (D_L**2) * ((d_theta / dz) ** 2)

P = np.zeros((M, N))

max_iteration = 2000
tolerance = 1e-5

for iteration in range(max_iteration):
    max_error = 0.0
    for i in range(1, M - 1):
        # h_bar = 1 + epsilon * cos(theta)
        h_i = 1.0 + epsilon * np.cos(theta[i])
        for j in range(1, N - 1):
            P_old = P[i, j]

            term1 = P[i + 1, j] + P[i - 1, j]
            term2 = (-(3.0 * d_theta / (2.0 * h_i)) * epsilon * np.sin(theta[i]) * (P[i + 1, j] - P[i - 1, j]))
            term3 = (epsilon * np.sin(theta[i]) / (h_i**3)) * (d_theta**2)
            term4 = C * (P[i, j + 1] + P[i, j - 1])
            denominator = 2.0 * (1.0 + C)
            P_new = (term1 + term2 + term3 + term4) / denominator

            if P_new < 0:
                P_new = 0.0
            P[i, j] = P_new

            error = abs(P_new - P_old)
            if error > max_error:
                max_error = error
    if max_error < tolerance:
        print(f"Solution converged after {iteration} iterations.")
        break
else:
    print("Maximum iterations reached without full convergence.")

plt.figure(figsize=(10, 6))
plt.plot(theta, P[:, N // 2], linewidth=2, label="Pressure at center (z=0.5)")
plt.title(f"Pressure Distribution at Bearing Center (L/D = {L_D}, e = {epsilon})")
plt.xlabel("Theta (radians)")
plt.ylabel("Non-Dimensional Pressure(P_bar)")
plt.grid()
plt.legend()
plt.show()
