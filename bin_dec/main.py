def dec_to_bin(num):
    ans = ""

    while num >= 1:
        x = num % 2
        num //= 2
        ans = str(x) + ans

    return ans


print(dec_to_bin(11))
print(dec_to_bin(7))
print(dec_to_bin(15))