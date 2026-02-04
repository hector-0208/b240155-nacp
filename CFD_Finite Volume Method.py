import numpy as np
import matplotlib.pyplot as plt
N = 9
X = 1
h = (X / (N - 1))
T = np.zeros(N)
T[N-1] = 1
T_new = np.zeros(N)
T_new[N-1] = 1
n_error = 1
iterations = 0
epsilon = 1e-8

while n_error > epsilon:
    for i in range (1,(N-1)):
        T_new[i] = (0.5*(T[i+1]+T[i-1]))
        T_new[i] = np.round(T_new[i], decimals=3)

    n_error = 0
    for i in range (1,(N-1)):
        n_error = n_error + abs(T[i] - T_new[i])
    iterations = iterations + 1
    T = T_new.copy()
print([T])
print(iterations)

x = np.arange(N) * h
plt.plot(x,T,'bo-')
plt.grid(True, color = 'r')
plt.title("T(X)")
plt.show()
