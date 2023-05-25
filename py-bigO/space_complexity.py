"""
What causes space complexity?
    - variables
    - data structures
    - function call
    - allocations
"""


def booooo(n):
    for i in range(len(n)):
        print("boooooo")

booooo([1,2,3,4,5]) # O(1)


def hi_n_times(n):
    hi_arr = [] # O(1)
    for i in range(n):
        hi_arr.append("hi") # O(n)
    return hi_arr

print(hi_n_times(6)) # O(n)
