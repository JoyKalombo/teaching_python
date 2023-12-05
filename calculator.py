def calculator(a, b, operator):
    if operator == "+":
        print(a + b)
    elif operator == "-":
        print(a - b)
    elif operator == "product":
        print(a * b)
    elif operator == "quotient":
        print(a / b)
    else:
        print("Enter one of the four words correctly :-)")

a = int(input('Enter 1st number: '))
c = str(input('Enter +, -, *, or /: '))
b = int(input('Enter 2nd number: '))
