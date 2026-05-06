def diff_with_rev(number):
    original = number
    reversed_number = 0
    while number:
        remainder = number % 10
        reversed_number = reversed_number * 10 + remainder
        number //= 10
    return abs(reversed_number - original)

num = int(input("Enter a number: "))
print(f"The difference of {num} from it's reverse is {diff_with_rev(num)}")
