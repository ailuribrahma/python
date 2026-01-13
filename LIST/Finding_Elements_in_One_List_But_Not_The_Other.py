list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

difference_list = list(set(list_a) - set(list_b))
print("difference_between_from_list_b : ",difference_list)  

# Item in either list but not both (Symmetric Difference)
symmetric_difference = list(set(list_a) ^ set(list_b))
print("Symmetric Difference : ", symmetric_difference)