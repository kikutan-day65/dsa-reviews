import array as arr

# creating an array with integer
a = arr.array('i', [1, 2, 3])

# printing original array
print("The new created array is: ", end=' ')
for i in range(len(a)):
    print(a[i], end=' ')

print()

# createing an array with double type
b = arr.array('d', [2.5, 3.2, 3.3])

# printing original array
print("The new created array is: ", end=' ')
for i in range(len(b)):
    print(b[i], end=' ')