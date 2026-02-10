def factorial(x):
    fact = 1
    if x == 1 or x == 0:
        return 1
    for i in range(1, x + 1):
        fact *= i
    return fact
    
n = int(input("Enter no. of terms: "))
sum_of_series = 0
for i in range(1, n + 1):
    sum_of_series += factorial(i)
print(f"Sum of the Series is {sum_of_series}")
# print(f"Factorial of {n} is {factorial(n)}")
