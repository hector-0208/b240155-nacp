def f(x):
    # Example function: x^2 - 10 = 0
    # (Root should be sqrt(10) ≈ 3.162)
    return x**2 - 10

def df(x):
    return 2*x

def newton_raphson(guess, tolerance=1e-6, max_iter=100):
    x = guess
    print(f"{'Iteration':<10} {'x_value':<10} {'Error'}")
    
    for i in range(max_iter):
        x_new = x - f(x) / df(x)
        
        error = abs(x_new - x)
        print(f"{i+1:<10} {x_new:<10.6f} {error:.6f}")
        
        if error < tolerance:
            return x_new
        x = x_new
        
    return x

initial_guess = 3.0
root = newton_raphson(initial_guess)
print(f"Calculated Root: {root}")
