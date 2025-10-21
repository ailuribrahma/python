my_list = input("Enter numbers separated by spaces: ")
nums = list(map(int, my_list.split()))
print("the list of numbers is:", nums)
full_set = set(range(min(nums), max(nums) + 1))  # Create a set of all numbers in the range
print("Full set of numbers from min to max:", full_set)



