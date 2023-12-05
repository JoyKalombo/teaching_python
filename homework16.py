# Task: Python List Manipulation
# Objective:
# The objective of this task is to practice working with lists in Python. Participants will perform various operations on lists, including element manipulation, appending, sorting, and filtering.
# Instructions:
# * Create a List:
#     * Create an empty 
#     * list named my_list.
my_list = []

# * Add Elements:
#     * Add the following elements to the list:
#         * "apple", "banana", "cherry", "date", "fig"
my_list.extend(["apple", "banana", "cherry", "date", "fig"])

# * Print the List:
#     * Print the current state of my_list.
print(my_list, "\n")

# * Access and Modify:
#     * Access the third element in the list and print it.
print("the third element is: ", my_list[2], "\n")

#     * Modify the fourth element to "grape" and print the updated list.
my_list[3] = "grape"
print("The list with the new new fourth element is ", my_list, "\n")

# * Append and Extend:
#     * Append "kiwi" to the end of the list.
my_list.append("kiwi")

#     * Create a new list named additional_fruits with elements "lemon" and "mango".
additional_fruits = ["lemon", "mango"]

#     * Extend my_list with the elements of additional_fruits.
my_list.extend(additional_fruits)

#     * Print the updated my_list.
print(my_list)

# * Sort the List:
#     * Sort my_list in alphabetical order.
my_list.sort()

#     * Print the sorted list.
print("The sorted list printed is ", my_list, "\n")

# * Remove Element:
#     * Remove "banana" from the list.
my_list.remove("banana")

#     * Print the updated list.
print("The list with \"banana\" removed is ", my_list, "\n")

# * Filter Elements:
#     * Create a new list named filtered_list that contains only the elements starting with the letter "a" from my_list.
filtered_list = [i for i in my_list if i[0] == "a"]

#     * Print filtered_list.
print("The list with only elements that begin with \"a\" is: ", filtered_list, "\n")

# * List Length:
#     * Print the length of my_list.
print("The length of my_list is ", len(my_list), "\n")

# * Clear the List:
my_list.clear()
# * Clear all elements from my_list.

# * Print the empty list.
print(my_list)

# Note:
# * Ensure that each step is implemented correctly before moving on to the next one.
# * Use built-in list methods for operations such as appending, sorting, and removing elements.
# * Comment your code appropriately to explain each step.
# * KEEP IT COOL!!!
# *  
