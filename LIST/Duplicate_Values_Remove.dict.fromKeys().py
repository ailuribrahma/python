# using dict.fromkeys() method to remove duplicates from a list while maintaining order from python 3.7+
my_List = [20, 30, 40, 50, 20, 30, 40]
unique_list = list(dict.fromkeys(my_List))
print("Original List:", my_List)
print("List after removing duplicates:", unique_list)