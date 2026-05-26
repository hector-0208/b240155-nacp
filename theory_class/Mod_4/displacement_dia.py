import matplotlib.pyplot as plt
import numpy as np

h = 50
N = 101

theta1 = np.linspace(0, 120, N)
theta_dwell1 = np.linspace(120, 180, N)
theta2 = np.linspace(180, 270, N)
theta_dwell2 = np.linspace(270, 360, N)

theta_rise = np.linspace(0, 180, N)
y_rise = (h / 2) * (1 - (np.cos(np.radians(theta_rise))))
y_fall = np.flip(y_rise)
y_dwell1 = np.full_like(theta_dwell1, h)
y_dwell2 = np.zeros_like(theta_dwell2)

plt.figure(figsize=(10, 6))
plt.xticks(np.arange(0, 361, 60))
plt.yticks(np.arange(0, h + 1, 5))
plt.title("Displacement Diagram")
plt.xlabel("Theta")
plt.ylabel("Lift")
plt.plot(theta1, y_rise, label="Ascent")
plt.plot(theta_dwell1, y_dwell1, label="Dwell 1")
plt.plot(theta_dwell2, y_dwell2, label="Dwell 2")
plt.plot(theta2, y_fall, label="Descent")
plt.grid()
plt.legend()
plt.show()
