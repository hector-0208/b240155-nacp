import matplotlib.pyplot as plt
import numpy as np

L = 6.0
N = 1000
x = np.linspace(0, L, N)
V = np.zeros_like(x)
M = np.zeros_like(x)

P1 = 30
P2 = 50
Ra = 56
Rb = 24

for i, pos in enumerate(x):
    if pos < 1:
        V[i] = -P1
    elif pos < 4:
        V[i] = -P1 + Ra
    else:
        V[i] = -P1 + Ra - P2
    if pos <= 1:
        M[i] = -P1 * pos
    elif pos <= 4:
        M[i] = -P1 * pos + Ra * (pos - 1)
    else:
        M[i] = -P1 * pos + Ra * (pos - 1) - P2 * (pos - 4)

# Plot SFD
plt.figure(figsize=(10, 8))
plt.subplot(2, 1, 1)  # Stack the plots
plt.plot(x, V, color="red")
plt.fill_between(x, V, 0, color="red", alpha=0.3)
plt.axhline(0, color="black")
plt.title("Shear Force Diagram (SFD)")
plt.ylabel("Shear Force")
plt.grid(True)

# Plot BMD
plt.subplot(2, 1, 2)
plt.plot(x, M, color="blue")
plt.fill_between(x, M, 0, color="blue", alpha=0.3)
plt.axhline(0, color="black")
plt.title("Bending Moment Diagram (BMD)")
plt.xlabel("Length")
plt.ylabel("Moment")
plt.grid(True)

plt.tight_layout()
plt.show()
