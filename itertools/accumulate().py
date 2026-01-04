import itertools
#similar operation like numpy's accumulate function
import numpy as np

numbers = [1,2,3,4,5,6]
print(list(itertools.accumulate(numbers)))
#Output: [1, 3, 6, 10, 15, 21]
#by default it performs addition
print(list(itertools.accumulate(numbers, lambda x, y: x * y)))
#Output: [1, 2, 6, 24, 120, 720]
#it performs multiplication
print(list(itertools.accumulate(numbers, lambda x,y: x**2 + y**2)))
#Output: [1, 5, 34, 1172, 1373609, 1886801684917]
#it performs x^2 + y^2 operation

new_matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(new_matrix)

