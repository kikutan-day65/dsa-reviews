"""
nCr = n! / r!(n-r)!
"""

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def combination(n, r):
    dividend = factorial(n)
    divisor = factorial(r) * factorial(n - r)

    answer = dividend // divisor
    return answer

res = combination(4, 2)
print(res)

res = combination(100, 5)
print(res)
