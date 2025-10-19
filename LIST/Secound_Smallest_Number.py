#using set() and sort() function to find second smallest number in list
my_list = input("Enter numbers separated by spaces: ")
nums = list(map(int, my_list.split()))
print("the list of numbers is:", nums)
unique_nums = list(set(nums))  # Remove duplicates by converting to a set and back to a list
print("List after removing duplicates:", nums)
unique_nums.sort()  # Sort the list in ascending order
print("Sorted list:", unique_nums)
if len(unique_nums) >= 2:
    second_Smallest = unique_nums[1]  # The second smallest element
    print("The second smallest number is:", second_Smallest)
else:
    print("There is no second smallest number (not enough unique elements).")