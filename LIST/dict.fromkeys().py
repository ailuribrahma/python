#dict.fromkeys method is used to remove duplicates from the list
my_list_1 = [10, 2, 4, 2, 10, 33, 45, 4, 6, 7, 45, 8, 9]
my_list_2 = ['a', 'b', 'c', 'a', 'd', 'b', 'e', 'f', 'c']
print("Original list 1:", my_list_1)
print("Original list 2:", my_list_2)    
unique_list_1 = list(dict.fromkeys(my_list_1))
unique_list_2 = list(dict.fromkeys(my_list_2))
print("List 1 after removing duplicates:", unique_list_1)
print("List 2 after removing duplicates:", unique_list_2)   