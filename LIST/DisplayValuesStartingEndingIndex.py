
# The list we will be working with
my_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print(f"Original list: {my_list}")


# Get the starting index from the user
try:
    start_index = int(input("Enter the starting index: "))
    end_index = int(input("Enter the ending index: "))
    if 0<=start_index<len(my_list) and 0<=end_index<=len(my_list) and start_index <= end_index:
    # Display the sublist
     print("List values from index", start_index, "to", end_index, "are:")
    print(my_list[start_index:end_index])  # end_index is exclusive
except ValueError:
    print("Invalid input. Please enter whole numbers only.")
    # You might want to exit or retry the process here
    exit()