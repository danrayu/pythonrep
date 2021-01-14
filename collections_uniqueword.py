from collections import Counter
s = 'In addition to the above, deques support iteration, pickling, len(d), reversed(d), copy.copy(d), copy.deepcopy(d),' \
    ' membership testing with the in operator, and subscript references such as d[0] to access the first element.' \
    'Indexed access is O(1) at both ends but slows to O(n) in the middle. For fast random access, use lists instead.'
print("Most common three characters of the said string:")
array = s.split(' ')
print(Counter(array).keys())