def calculator(a, b, operator):
    if operator == "+":
        result = a + b
        print(result)
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        result = a / b
    
    return result

a = int(input('Enter 1st number: '))
operator = input('Enter +, -, *, or /: ')
b = int(input('Enter 2nd number: '))

calculator_result = calculator(a, b, operator)

print(calculator_result)