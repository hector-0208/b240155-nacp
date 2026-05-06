lower_lim = int(input("Enter the lower limit of the range: "))
upper_lim = int(input("Enter the upper limit of the range: "))
n = int(input("Enter the value of n: "))
res = []
for i in range(lower_lim, upper_lim + 1):
    if i % n == 0 and i % n**2 != 0:
        res.append(i)
print(f"The required list is {res}")
