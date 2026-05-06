a = [1, 3, 5, 7, 8, 10]
target = 7
# Binary Search:
left = 0
right = len(a) - 1
while left <= right:
    mid = (left + right) // 2
    if a[mid] == target:
        print(f"Found {target} at index {mid}")
        break
    elif a[mid] > target:
        right = mid - 1
    else:
        left = mid + 1
# Linear Search:
for i in range(len(a)):
    if a[i] == target:
        print(f"Found {target} at index {i}")
        break
