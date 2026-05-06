months = {"jan": 1, "feb": 2, "mar": 3}
for month in months.keys():
    print(month, end=" ")
for day in months.values():
    print(day, end=" ")
print()

print(list(months.keys()))
print(list(months.values()))
print(list(months.items()))

for month in sorted(months.keys()):
    print(month, end=" ")
print()

months.update({"apr": 4})
print(months)
