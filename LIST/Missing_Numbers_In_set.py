list1 = input("enter numbers separated by spaces: ")
nums = list(map(int, list1.split()))
print("the list of numbers is:", nums)
full_set = set(range(min(nums), max(nums) + 1))  # Create a set of all numbers in the range
print("Full set of numbers from min to max:", full_set)
missing_numbers = full_set - set(nums)  # Find the missing numbers by set difference
print("Missing numbers in the list are:", sorted(missing_numbers))  # Print missing numbers