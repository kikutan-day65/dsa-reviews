"""
Rules:
    1. Always worst case
    2. Remove constants
    3. Different inputs should have different variables. O(a+b).
       A and B arrays nested would be O(a*b)
       + for steps in order
       + for nested steps
    4. Drop Non-dominat terms
"""


char_arr = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k'
]

num_arr = [1,2,3,4,5,6,7,8,9]


# O(n) -> Linear time
def linear_time(arr):
    for i in range(len(arr)):
        if arr[i] == 'k':
            print("Found k!")


# O(1) -> constant_time
def constant_time(arr):
    print(arr[0]) 


# O(n + m) -> different terms for input
def different_terms1(n, m):
    for i in range(n):
        print(i, end=' ')
    
    print()

    for j in range(m):
        print(j, end=' ')


# O(n * m) -> different terms for input
def different_terms2(n, m):
    for i in range(n):
        print(i, end=' ')
        for j in range(m):
            print(j, end=' ')
        print()


# O(n^2) -> quadratic time
def quadratic_time(arr):
    for i in range(len(arr)):
        print()
        for j in range(len(arr)):
            print(arr[i] + arr[j], end=' ')


# O(n!) -> factorial time
# You may not encounter this terreble time complexity

linear_time(char_arr)
print()

constant_time(char_arr)
print()

different_terms1(4, 5)
print()

different_terms2(4, 5)
print()

quadratic_time(num_arr)
print()

