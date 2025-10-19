my_list = input("Enter numbers separated by spaces: ")
nums = list(map(int, my_list.split()))
print("The list of numbers is:", sum(nums))
