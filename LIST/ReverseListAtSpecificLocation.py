# Define a function to reverse a portion of a list in place
def reverse_list_in_location(lst):
    start_pos
    end_pos
    
    # Use a while loop to swap elements from the start and end positions
    while start_pos < end_pos:
        #print(type(lst))
        # Swap elements at start_pos and end_pos using tuple unpacking
        lst[start_pos], lst[end_pos] = lst[end_pos], lst[start_pos]
        # Move the start_pos towards the end_pos and vice versa
        start_pos += 1  
        print (type(start_pos))
        #print(type(start_pos))
        end_pos -= 1
    # Return the modified list
    return lst
  
# Create a list of numbers
nums = ['brahma', 'nani', 'arjun', 'krishna', 'divya', 'reddy', 'man', 'fat']
# Define the start and end positions for the first reverse operation
print("Enter Starting value")
start_pos = int(input())
print("Enter ending value")
end_pos = int(input())

# Print the original list
print("Original list:")
print(nums)

# Print a message indicating which portion of the list will be reversed
print("Reverse elements of the said list between index position " + str(start_pos) + " and " + str(end_pos))

# Call the reverse_list_in_location function and print the result
print(reverse_list_in_location(nums))

# # Define the start and end positions for the second reverse operation
# start_pos = 6
# end_pos = 7

# # Print a message indicating which portion of the list will be reversed
# print("\nOriginal list:")
# print(nums)
# print("Reverse elements of the said list between index position " + str(start_pos) + " and " + str(end_pos))

# # Call the reverse_list_in_location function again and print the result
# print(reverse_list_in_location(nums, start_pos, end_pos))

# # Define the start and end positions for the third reverse operation
# start_pos = 0
# end_pos = 7

# # Print a message indicating which portion of the list will be reversed
# print("\nOriginal list:")
# print(nums)
# print("Reverse elements of the said list between index position " + str(start_pos) + " and " + str(end_pos))

# # Call the reverse_list_in_location function once more and print the result
# print(reverse_list_in_location(nums, start_pos, end_pos)) 