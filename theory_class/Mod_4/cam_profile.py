import matplotlib.pyplot as plt
import numpy as np

N = 301
R_b = 50
h = 50

alpha = 120
dwell1 = 60
beta = 60

theta_rise = np.linspace(0, alpha, N)
theta_dwell1 = np.linspace(alpha, alpha + dwell1, N)
theta_return = np.linspace(alpha + dwell1, alpha + dwell1 + beta, N)
theta_dwell2 = np.linspace(alpha + dwell1 + beta, 360, N)

theta_lift = np.linspace(0, 180, N)

y_rise = (h / 2) * (1 - (np.cos(np.radians(theta_lift))))
y_dwell1 = np.full_like(theta_dwell1, h)
y_fall = np.flip(y_rise)
y_dwell2 = np.zeros_like(theta_dwell2)

theta = np.concatenate([theta_rise, theta_dwell1, theta_return, theta_dwell2])
y_total = np.concatenate([y_rise, y_dwell1, y_fall, y_dwell2])

theta_rad = np.radians(theta)

r = R_b + y_total
x = r * np.cos(theta_rad)
y = r * np.sin(theta_rad)

x_base = R_b * np.cos(theta_rad)
y_base = R_b * np.sin(theta_rad)


plt.figure(figsize=(6, 6))
plt.axis("equal")
plt.title("Cam Profile")
plt.plot(x, y, label="Cam Profile")
plt.plot(x_base, y_base, '--', label="Base Circle")
plt.legend()
plt.show()
