
# 1. **Variable Practice:**
#    Create variables for a person's name, age, and favorite hobby. Print a message using these variables.

name = "Junior"
age = 25
favourite_hobby = "playing basketball"
print(f"Hello! My name is {name}. I am {age} years old and my favourite hobby is {favourite_hobby}. \n") 



# 2. **User Input:**
#    Use the `input` function to get the user's favorite color. Print a message incorporating this input.

favourite_colour = input("Type your favourite colour: ")
print(f"Your favourite colour is... {favourite_colour} \n") 



# 3. **Conditional Statements:**
#    Write a program that asks the user for a number. If it's even, print a message saying so; if odd, print a different message.
 
user_number = float(input("Enter a number: "))
if user_number % 2 == 0:
    print(f"{user_number} is an even number \n")
else:
    print(f"{user_number} is not an even number \n")



# 4. **List Manipulation:**
#    Create a list of your favorite fruits. Print the first and last elements of the list.

favourite_fruits = ["apple", "banana", "cherry", "dates", "fig", "grapes"]
print(f"The first fruit is... {favourite_fruits[0]} & the last fruit is... {favourite_fruits[-1]}")



# 5. **Loops:**
#    Use a loop to print the numbers from 1 to 5. Then modify it to print only the even numbers.

for i in range(1,6):
    print(i)

print('\n')

for i in range(1,6):
    if i % 2 == 0:
        print(i)

print('\n')


# 6. **Function Definition:**
#    Define a function that takes two parameters (numbers) and returns their sum. Call the function with different arguments.
 
def sum(a,b):
    print(a+b)
    return a+b
sum(2,5)
sum(20,50)

print('\n')


# 7. **String Manipulation:**
#    Take a sentence as a string and print it in reverse order.
 
sentence = "This is a sentence I am writing."
# print(sentence[-1:])
reverse_sentence = ''
for i in range(1, len(sentence)+1):
    reverse_sentence += sentence[-i]
print(reverse_sentence)
print('\n')


# 8. **Dictionary Exercise:**
#    Create a dictionary with at least three key-value pairs (e.g., 'name': 'John'). Print one of the values using its corresponding key.

person = {
    'Name' : 'John',
    'Age' : 34,
    'Occupation' : 'Doctor'
}
print(person['Name'])
print('\n')


# 9. **File Handling:**
#    Open a new text file, write a few lines to it, and then close the file. Open the file again, read its contents, and print them.
 
my_file = 'file.txt'
with open(my_file, 'w') as file:
    file.write(f"I am testing the first line. \nI am writing a second line. \nI am writing a third line. \n")
    
with open(my_file, 'r') as file:
    print(file.read())

# 10. **Error Handling:**
#     Write a program that asks the user for input. Use a try-except block to catch any errors that might occur (e.g., if the user enters a non-numeric value). If an error occurs, print a friendly error message.

max_attempts = 3
 
while max_attempts > 0:
    try:
        user_input = int(input("Enter a positive integer: "))
        if user_input > 0:
            print("You entered:", user_input)
            break
        else:
            print("Error: Please enter a positive integer.")
    except ValueError:
        print("Error: Please enter a valid integer.")
 
    max_attempts -= 1
    print(f"{max_attempts} attempts remaining.")
 
if max_attempts == 0:
    print("You've exceeded the number of attempts. Exiting the program.")
 
 
