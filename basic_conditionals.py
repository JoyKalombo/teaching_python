def calculator(a, b, operator):
    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        result = a / b
    elif operator == "^":
        result = a**b
    
    return result

a = float(input('Enter 1st number: '))
operator = input('Enter +, -, *, ^, or /: ')
b = float(input('Enter 2nd number: '))

calculator_result = calculator(a, b, operator)

print(calculator_result)