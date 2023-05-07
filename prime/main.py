import math

def is_prime(num):
    x = math.sqrt(num)
    y = int(x)

    for i in range(2, y + 1):
        if num % i == 0:
            return False
    return True

print("53: ", is_prime(53))
print("111: ", is_prime(111))
print("5: ", is_prime(5))
print("1327: ", is_prime(1327))