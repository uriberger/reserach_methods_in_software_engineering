''' This function receives a decimal integer and returns a binary representation. '''

def long_decimal_to_binary(num):
    res = 0
    power = 0
    if num < 0:
        num = num * (-1)
    while num > 0:
        if num % 2 == 1:
            res = res + 10**power
            num = num - 1
        power = power + 1
        num = num / 2
    return res

def short_decimal_to_binary(num):
    res = 0
    power = 0
    num = num * (-1) if num < 0 else num
    while num > 0:
        if num % 2 == 1:
            res += 10**power
            num -= 1
        power += 1
        num /=  2
    return res

print(long_decimal_to_binary(43))
print(short_decimal_to_binary(43))