#How to take input from user and store in list?
#use the built-in input() function to take input from the user.
#Then, you can split the input string into individual elements and convert them to the desired data
#type (e.g., integers or floats) before storing them in a list.
#Here is an example code that demonstrates how to take input from the user and store it in a list:
# Initialize an empty list to store the numbers

user_input_string = input("Enter numbers separated by spaces: ")
my_list = user_input_string.split()
print("the list of numbers is:", my_list)

#handle different data types
#If you want to store numbers as integers or floats, you can use the map() function
#to convert the input strings to the desired type before storing them in the list.
#Here is an example that takes input as integers:

user_input_string = input("Enter numbers separated by spaces: ")
my_number_list = [int(item) for item in user_input_string.split()]
print("the list of numbers is:", my_number_list)
