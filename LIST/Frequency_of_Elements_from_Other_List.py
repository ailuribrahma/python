from collections import Counter
a = [0,1,2,2,3,4,2,5,3,1]
b = [0,1,2,3,4,5,6,7,8,9]
freq = Counter(a)
result = {key: freq[key] for key in b}
print("Frequency of elements from list 'b' in list 'a':", result)