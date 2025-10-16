my_list = [10, 2, 33, 45, 6, 7, 8, 9]
largest = smallest = my_list[0]
for num in my_list:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("Original list:", my_list)
print("Largest number in the list is:", largest)
print("Smallest number in the list is:", smallest)