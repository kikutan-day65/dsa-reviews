# euclid algorithm

def gcd(num1, num2):
    while num1 >= 1 and num2 >= 1:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    if num2 >= 1:
        return num2
    return num1

result = gcd(33, 88)
print(result)

result = gcd(123, 777)
print(result)

result = gcd(12, 8)
print(result)