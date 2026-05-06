import numpy as np

# 1. Setup
n = 11                        # Number of points (from board "n=11")
h = 0.3                       # Step size (from board "h=3/10")
x = np.linspace(0, 3, n)      # Create x points: 0, 0.3, ... 3.0
f = np.zeros(n)               # Create array for f(x), initially all 0

# 2. Boundary Conditions (from board)
f[0] = 0.0      # f(0) = 0
f[-1] = 2.0     # f(3) = 2

# 3. Solve (Iterative Method)
# Run 100 times to make sure it converges
for k in range(100):
    for i in range(1, n - 1):  # Loop through internal points only
        # The formula from the board:
        # f(xi) = [ f(xi+1) + f(xi-1) - h^2 * (xi^2 - 2) ] / 2
        f[i] = 0.5 * (f[i+1] + f[i-1] - h**2 * (x[i]**2 - 2))

# 4. Print Results
print("   x   |   f(x)")
print("-------|---------")
for i in range(n):
    print(f" {x[i]:.1f}   |  {f[i]:.5f}")
