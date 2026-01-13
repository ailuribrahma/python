from collections import Counter
a = [1,2,2,3,4,2,5,3,1]
b = [1,2,3]
freq = Counter(a)
result = {key: freq[key] for key in b}
print("Frequency of elements from list 'b' in list 'a':", result)