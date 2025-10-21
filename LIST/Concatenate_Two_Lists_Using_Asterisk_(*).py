#this is a modern way to concatenate two lists using the asterisk (*) operator 
# to unpack the elements of both lists into a new list.
#introduced in Python 3.5
list1 = [10, 20, 30]
list2 = [40, 50, 60]
concatenated_list = [*list1, *list2]
print("Concatenated List using * operator:", concatenated_list)