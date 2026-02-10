def max_of_three(num1, num2, num3):
    max = num1
    if num2 > max:
        max = num2
    elif num3 > max:
        max = num3
    return max
    
print(max_of_three(-1, -4, -2.3))
