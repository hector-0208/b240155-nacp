import matplotlib.pyplot as plt

def f(xx):
    C = (11 - 81/12) / 3
    return(xx**4/12 - xx**2 + C*xx)

x = 0
dx = 0.1
fa_x = []
fa_y = []
# i = 0
while x < 3:
    fa_x.append(x)
    fa_y.append(f(x))
    # print(f"f_ax and f_ay at index {i} is {fa_x[i]}, {fa_y[i]}")
    # i += 1
    x += dx

h = 0.2
xp = []
# i = 0
# while i < (3 + h):
#     xp += [i]
#     i += h
n = 30
for i in range(n):
    xp.append(i)
    
m = 2 / 3
fp = []
fp2 = []

for i in range(len(xp)):
    fp += [m * xp[i]]
    fp2 += [m * xp[i]]

n = 0
N = 200

while n < N:
    for i in range(1, len(xp) - 1):
        fp2[i] = 0.5 * (fp[i + 1] + fp[i - 1] - h ** 2 * (xp[i] ** 2 - 2))
    
    for i in range(len(xp)):
        fp[i] = fp2[i]
    n += 1


exact_val = f(3)
second_deriv = (fp[-1] - 2*fp[-2] + fp[-3]) / (h**2)
print(f"Exact Double Derivative at x = 3: {exact_val:.5f}")
print(f"Numerical Derivative at x = 3:    {second_deriv:.5f}")

plt.figure(figsize=(8, 5))

plt.plot(fa_x, fa_y, color='red', label='Analytical Solution')

plt.plot(xp, fp, color='blue', marker='o', label='Numerical Sollution')

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
