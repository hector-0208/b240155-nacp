import numpy as np
import matplotlib.pyplot as plt

L = 3.0
a1 = 1.5
P = 150
Ay = 150


Mb_Ay = Ay * a1       # positive
Mb_BD = -450          # negative
Mb_total = Mb_Ay + Mb_BD

# Domain
x = np.linspace(0, L, 500)

# Shear Force calculations
V = np.full_like(x, Ay)
V[x >= L] = 0  # Assuming it drops to zero at the end

# Bending Moment calculations
M = Ay * x
# Apply the moment step change after a1
M[x >= a1] += (Mb_total - Ay * a1)

# Plot SFD
plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1) # Stack the plots
plt.plot(x, V, color='red')
plt.fill_between(x, V, 0, color='red', alpha=0.3)
plt.title("Shear Force Diagram (SFD)")
plt.ylabel("Shear Force")
plt.grid(True)

# Plot BMD
plt.subplot(2, 1, 2)
plt.plot(x, M, color='blue')
plt.fill_between(x, M, 0, color='blue', alpha=0.3)
plt.title("Bending Moment Diagram (BMD)")
plt.xlabel("Length")
plt.ylabel("Moment")
plt.grid(True)

plt.tight_layout()
plt.show()
