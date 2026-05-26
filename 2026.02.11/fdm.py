n = 100
x_n = 3
x_0 = 0

h = (x_n - x_0) / (n - 1)

x = [x_0 + h * i for i in range(n)]
f = [0 for i in range(n)]
f[0] = 0
f[n - 1] = 2

max_iteration = 500
for iteration in range(max_iteration):
    for i in range(1, n - 1):
        f[i] = 0.5 * (f[i + 1] + f[i - 1] - h**2 * (x[i] ** 2 - 2))
print("x\tf(x)")
for i in range(n):
    print(f"{x[i]:.2f}\t{f[i]:.6f}")
print(f"f(1) = {1**4 / 12 - 1**2 + 17 / 12 * 1}")
      