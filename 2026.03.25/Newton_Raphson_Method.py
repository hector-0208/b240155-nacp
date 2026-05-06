def f(x):
    # return x**2 - 2
    # return math.exp(-x) - x
    return x**3 - 2 * x**2 - 4 * x + 8


def df(x):
    # return 2 * x
    # return -(math.exp(-x)) - 1
    return 3 * x**2 - 4 * x - 4


def newton_raphson(guess, tolerance=1e-4, max_iteration=100):
    x = guess
    error = 100
    i = 1
    # print(f"{'Iteration'}{'x_new':>15}{'error':>15}")
    while error > tolerance:
        if abs(df(x)) < 1e-10:
            print(f"Derivative reached zero at iteration {i}")
            print(f"The last value of x was {x}")
            return None
        x_new = x - (f(x) / df(x))
        error = abs(x_new - x)
        # print(f"{i:>9} {x_new:>15.8f} {error:>15.8f}")
        i += 1
        x = x_new
        if i > max_iteration:
            print("Maximum iterations reached")
            break
    return x_new


roots = []
left = -1
right = 1
n = 10
for i in range(n):
    # print(f"\nTrying initial guess = {guess}")
    root = newton_raphson(left)
    if root is not None:
        root = round(root, 4)
    if root not in roots:
        roots.append(root)
    left -= 1
    
    root = newton_raphson(right)
    if root is not None:
        root = round(root, 4)
    if root not in roots:
        roots.append(root)
    right += 1

# print(f"The root is {newton_raphson(initial_guess):.8f}")
for r in roots:
    print(f"f-> {r}")
