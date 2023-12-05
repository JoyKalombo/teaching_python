import random as r
 
def is_integer(value):
    return int(value) == value
 
def calculator():
    print("The Calculator")
    print("I'll add a touch of humor to your calculations. Let's get started!")
 
    while True:
        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")
 
        choice = input("Enter the operation number (1-5): ")
 
        if choice == '5':
            print("Thanks for using the Funny Calculator. Have a great day!")
            break
 
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue
 
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
 
        result = 0
 
        if choice == '1':
            result = num1 + num2
            joke = r.choice(["Math is hard, but not for me!", "Adding numbers like a boss!", "The sum is looking fabulous!"])
        elif choice == '2':
            result = num1 - num2
            joke = r.choice(["Subtracting like a ninja!", "Is it subtraction or magic? You decide!", "The difference is as mysterious as my cat."])
        elif choice == '3':
            result = num1 * num2
            joke = r.choice(["Multiplying like a genius!", "The product is as shiny as a unicorn.", "Mathematics at its finest!"])
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                joke = r.choice(["Dividing and conquering!", "The quotient is as impressive as a superhero.", "Mathematics in motion!"])
            else:
                print("Error: Cannot divide by zero. Please choose different numbers.")
                continue
            
        if is_integer(result):
            result = int(result)
            result_str = str(result)
        else:
            result_str = "{:.2f}".format(result)
 
        print(f"\nResult: {result_str}")
        print(f"Humor: {joke}")
 
 
 
if __name__ == "__main__":
    calculator()
 