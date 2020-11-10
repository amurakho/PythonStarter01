d = {}

d.get('key')

d['key']



import numpy

a = numpy.array([
    [1, 2, 3, 4, 5, 6, 7, 8],
    [9, 10, 11, 12, 13, 14, 15, 16]
])
new_a = a
new_a[0, 0] = a.copy()
print(a)
print(new_a)

b = a
b[0, 0] = 300

print(a)
print(b)

b.shape = (2, 2, 4)
print('A')
print(a)
print('B')
print(b)

