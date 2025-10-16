# Define a function to generate all permutations of a list of numbers
def permutations(nums):
    # Base case: If the input list is empty, return an empty list as there are no permutations.
    if len(nums) == 0:
        return []
    # Base case: If the input list has only one element, return a list containing that element as the only permutation.
    if len(nums) == 1:
        return [nums]
    # Initialize an empty list 'result' to store permutations.
    result = []
    # Iterate over the elements of the input list.
    for i in range(len(nums)):
        # Select an element 'm' at index 'i'.
        m = nums[i]
        # Create a new list 'rem_list' that contains all elements except 'm'.
        rem_list = nums[:i] + nums[i+1:]
        # Recursively find permutations of 'rem_list'.
        for p in permutations(rem_list):
            # Add 'm' to the beginning of each permutation in 'p' and append it to the 'result' list.
            result.append([m] + p)
    # Return the list of all permutations.
    return result

# Create a list of numbers
user_input = input("Enter numbers separated by spaces: ")
nums = list(map(int, user_input.split()))
print("the list of numbers is:", nums)

# Print the original list
print("Original list:")
print(nums)

# Call the permutations function and print the result, which is a list of all permutations of 'nums'.
print("Permutations of the members of the said list:")
print(permutations(nums))

# # Create another list of numbers
# nums = [-100, -300, 0]

# # Print the original list
# print("\nOriginal list:")
# print(nums)

# # Call the permutations function with the second list and print the result, which is a list of all permutations of 'nums'.
# print("Permutations of the members of the said list:")
# print(permutations(nums)) 
