numbers = [2, 5, 7, 8, 9, 10]
loop = True
while loop:
    op = input("""\nSelect an operation:
                       +: add element
                       *: edit element
                       -: delete element
                       /: display list
                       =: stop\n""")
    match op:
        case "+":
            num = int(input("Enter value to add into list: "))
            numbers.append(num)
        case "*":
            index = int(input("Enter index of where you want to add an element: "))
            num = int(input("Enter value to add into list: "))
            numbers.insert(index, num)
        case "-":
            index = int(input("Enter index of element you want to delete: "))
            del numbers[index]
        case "/":
            print(f"The list is {numbers}")
        case "=":
            loop = False
        case _:
            print("Enter a valid operation.")
