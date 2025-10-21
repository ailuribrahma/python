#This extend() method is used to all the elements of one list to the end of another existing list. Unlike the + operator
#this method modifies the first list in-place and does not create a new list.
list1 = ['a', 'b', 'c']
list2 = ['d', 'e', 'f']
list3 = ['g', 'h', 'i']
list1.extend(list2)
list1.extend(list3)
list2.extend(list3)
print("Concatenated List using extend():", list1, list2)