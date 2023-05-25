"""
Given two arrays, create a function that let user know (true/false)
whether these two arrays contain any common items

For example:
    array1 = ['a', 'b', 'c', 'x']
    array2 = ['z', 'y', 'i']
    should return False
    --------------------------------
    array1 = ['a', 'b', 'c', 'x']
    array2 = ['z', 'y', 'x']
    should return True
"""

# time complexity: O(n + m)
# space complexity: O(n)
def has_common_item(arr1, arr2):

    array_hash = {}
    for i in range(len(arr1)):
        array_hash[arr1[i]] = None
    
    for j in range(len(arr2)):
        if arr2[j] in array_hash:
            # print("Common item:", arr2[j])
            return True
    return False


res = has_common_item(['a', 'b', 'c', 'x'], ['z', 'y', 'i'])
print(res)

res = has_common_item(['a', 'b', 'c', 'x'], ['z', 'y', 'x'])
print(res)