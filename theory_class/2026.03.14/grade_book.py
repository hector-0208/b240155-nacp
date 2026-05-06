grade_book = {
    "Susan": [92, 85, 100],
    "Eduardo": [83, 95, 79],
    "Azizi": [91, 89, 82],
    "Pantipa": [97, 91, 92],
}
sum_of_grades = 0
count = 0
for name, grade in grade_book.items():
    stu_avg = sum(grade) / len(grade)
    print(f"Average grade of {name} is {stu_avg}")
    sum_of_grades += sum(grade)
    count += len(grade)
total_avg = sum_of_grades / count
print(f"Average grades of students = {stu_avg}\n")
print(f"Total class average = {total_avg}")
