import array as arr

a = arr.array('i', [1, 2, 3, 1, 5, 4, 7, 9])

print("The new created array is : ", end="")
for i in range(len(a)):
    print(a[i], end=" ")
 
print("\r")

# remove an element with pop()
a.pop() # remove hte last element

a.pop(2)    # remove the 2nd index element

a.remove(1) # remove the 1st occurance of 1

print("The array after removing is : ", end="")
for i in range(len(a)):
    print(a[i], end=" ")