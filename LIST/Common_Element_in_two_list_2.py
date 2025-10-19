list1 = [12, 13 , 14, 15, 16]
list2 = [14, 15, 16, 17, 18]
common_elements = []
for element in list1:
    for element2 in list2:
        if element == element2:
            common_elements.append(element)
print("Common elements in both lists:", common_elements)
# Alternative approach using 'in' keyword
   # print(element)
#     if element in list2:
#         common_elements.append(element)
# print("Common elements in both lists:", common_elements)