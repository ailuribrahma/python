#This method allows the user to enter items one by one until they type a specific stop word (e.g., 'done' or 'quit').

print("Enter items one by one. Type 'done' when you are finished:")
my_dynamic_list = [] # Initialize an empty list to store the items
while True:
    user_input = input("enter item: ")
    if user_input.lower() == 'done': 
        break # Exit the loop 
    my_dynamic_list.append(user_input) # Add the input item to the list
    print(f"\nFinished taking inputs.")
    print(f"The list of items is: {my_dynamic_list}")