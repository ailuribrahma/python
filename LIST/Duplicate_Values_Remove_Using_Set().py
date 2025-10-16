#order will be changed because of set() method are unordered collection data type
#using set() method to remove duplicates from a list
My_List = [10, 20, 40, 40, 20]
print("Original List:", My_List)
unique_list = list(set(My_List))
print("List after removing duplicates:", unique_list)