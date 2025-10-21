Original_list = input("Enter numbers separated by spaces: ")
nums = list(map(int, Original_list.split()))
print("the list of numbers is:", nums)
new_list = nums.copy()  # Copying the original list to a new list
print("The copied list is:", new_list)
