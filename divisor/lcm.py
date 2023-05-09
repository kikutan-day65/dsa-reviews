def gcd(a, b):
    while a >= 1 and b >= 1:
        if a > b:
            a = a % b
        else:
            b = b % a
    if a >= 1:
        return a
    return b

def lcm(a, b, divisor):
    dividend = abs(a * b)
    return dividend // divisor


num1 = 2
num2 = 3
res = lcm(num1, num2, gcd(num1, num2))
print(res)


num1 = 132
num2 = 77
res = lcm(num1, num2, gcd(num1, num2))
print(res)