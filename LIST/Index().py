My_List = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
element = 'date'
try:
    index = My_List.index(element)
    print(f"The index of '{element}' is: {index}")
except ValueError:
    print(f"'{element}' is not in the list.")       