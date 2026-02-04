import numpy as np
import matplotlib.pyplot as plt
N = 51
L = 1
h = (L/(N-1))
iterations = 0
k = 0.1
A = 0.001

T = np.zeros((N,N))
T[0,:] = 1
T_new = np.zeros((N,N))
T_new[0,:] = 1
epsilon = 1e-8
numerical_error = 1

while numerical_error > epsilon:
    for i in range (1,N-1):
        for j in range (1, N-1):
            a_E = (k*A)/h
            a_W = (k * A) / h
            a_S = (k * A) / h
            a_N = (k * A) / h
            a_P = a_E + a_W + a_N + a_S
            T_new[i,j] = (a_E*T[i, j+1] + a_W*T[i, j-1] + a_N*T[i-1, j] + a_S*T[i+1, j])/a_P

    numerical_error = 0
    for i in range(1, N-1):
        for j in range(1, N-1):
            numerical_error = numerical_error + abs(T[i,j] - T_new[i,j])
    iterations = iterations + 1
    T = T_new.copy()
    print(T)
    if iterations % 1000 == 0:
        plt.figure(1)
        plt.semilogy(iterations, numerical_error, 'ko')
        plt.pause(0.02)

print("Iteration : ", iterations, "T = ", T )

x_dom = np.arange(N) * h
y_dom = L - np.arange(N) * h
[X,Y] = np.meshgrid(x_dom, y_dom)
plt.figure(2)
plt.contour(X, Y, T, 72)
plt.title("T(X,Y)")
plt.show()
