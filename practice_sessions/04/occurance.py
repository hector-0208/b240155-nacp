def find(n, nums):
    occurance = []
    for i in range(len(nums)):
        if nums[i] == n:
            occurance.append(i)
    if len(occurance) == 0:
        print("The inputted number is not in the list")
    else:
        print(f"All occurances of the inputted number in the list are {occurance}")
numbers = [0, 2, 4, 5, 2, 7]
num = int(input("Enter the number: "))
find(num, numbers)
        