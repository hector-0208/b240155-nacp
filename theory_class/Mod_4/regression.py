import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([1.2, 1.9, 3.2, 3.9, 5.1])

# Least Squares Calculations
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_x2 = np.sum(x**2)
sum_xy = np.sum(x * y)

# Slope (m) and Intercept (c)
m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
c = (sum_y - m * sum_x) / n

y_fit = m * x + c

print(f"Slope (m) = {m:.4f}, Intercept (c) = {c:.4f}")

# Plotting
plt.figure(figsize=(10, 6))
plt.title("Least Squares Method")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y_fit, label="Fitted curve (y = mx + c)")
plt.scatter(x, y, color='red', label="Actual values")
plt.legend()
plt.grid()
plt.show()
