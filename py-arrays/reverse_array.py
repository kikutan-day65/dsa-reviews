# time complexity: O(n)
# space complexity: O(1)

def reverse(arr):
    l = 0
    r = len(arr) - 1

    while l < r:
        temp = arr[l]
        arr[l] = arr[r]
        arr[r] = temp

        l += 1
        r -= 1
    
    return arr

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = arr = ['A', 'B', 'C', 'D']

print(reverse(arr1))
print(reverse(arr2))