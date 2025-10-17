#using set() and sort() function to find second largest number in list
my_list = input("Enter numbers separated by spaces: ")
nums = list(map(int, my_list.split()))
print("the list of numbers is:", nums)
unique_nums = list(set(nums))  # Remove duplicates by converting to a set and back to a list
print("List after removing duplicates:", nums)
unique_nums.sort()  # Sort the list in ascending order
if len(unique_nums) >= 2:
    second_largest = unique_nums[-2]  # The second largest element
    print("The second largest number is:", second_largest)
else:
    print("There is no second largest number (not enough unique elements).")    