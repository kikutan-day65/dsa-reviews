arr = ['a', 'b', 'c', 'd']


# append: O(1)
arr.append('e')
print(arr)


# pop: O(1)
arr.pop()
print(arr)


# prepend: O(n)
def prepend(arr):
    arr.insert(0, 'x')
    return arr

print(prepend(arr))


# insert middle: O(n)
def insert_middle(index, arr):
    arr.insert(index, 'A')
    return arr

print(insert_middle(3, arr))


# pop_middle: O(n):
def pop_middle(index, arr):
    arr.pop(index)
    return arr

print(pop_middle(2, arr))