n = int(input("Enter value of n: "))
# stars = 1
# space = n - 1
# for i in range(n):
#     print(" " * space, end="")
#     print("*" * stars, end="")
#     print('\n')
#     space -= 1
#     stars += 1
for i in range(n - 1, -1, -1):
    print(" " * (i), end='')
    print("*" * (n - i))

