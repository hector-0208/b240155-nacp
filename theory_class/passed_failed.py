num_students, passed, failed = 10, 0, 0
for i in range(num_students):
    result = int(input("Enter result: "))
    if result == 1:
        passed += 1
    else:
        failed += 1
print(passed, "students passed,", failed, "students failed")
if passed > 8:
    print("Bonus to the instructor.")
