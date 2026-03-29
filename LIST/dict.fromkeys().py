#dict.fromkeys method is used to remove duplicates from the list
my_list_1 = [10, 2, 4, 2, 10, 33, 45, 4, 6, 7, 45, 8, 9]
my_list_2 = ['a', 'b', 'c', 'a', 'd', 'b', 'e', 'f', 'c']
my_list_3 = ['brahma','nani','arjun','divya','krushna','reddy','barhma','arjun','divya','brahma']

#print original list
print("Original list 1:", my_list_1, "Original list 2:", my_list_2)
#using dict.fromkeys() method to remove duplicates from the list
print(list(dict.fromkeys(my_list_1)))
print(list(dict.fromkeys(my_list_2)))
