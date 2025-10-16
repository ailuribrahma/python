#using max() and min() methods to find largest and smallest number in a list
my_list = []
user_input = input("Enter numbers separated by spaces: ")
my_list = list(map(int, user_input.split()))
print("Original list:", my_list)
largest = max(my_list)
smallest = min(my_list)
print("Largest number in the list is:", largest)
print("Smallest number in the list is:", smallest)
      