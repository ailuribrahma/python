# Alternative approach using 'in' keyword
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]
common_elements = []
for element in list1:  
    if element in list2:
     common_elements.append(element)
print("Common elements in both lists:", common_elements)