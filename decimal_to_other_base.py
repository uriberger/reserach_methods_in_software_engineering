''' This function receives a decimal integer and returns a representation in another base. '''

def long_decimal_to_other_base(num,base):
    res = 0
    power = 0
    if num < 0:
        num = num * (-1)
    while num > 0:
        remainder = num % base
        cur_power_factor = 10**power
        cur_addition = remainder*cur_power_factor
        res = res + cur_addition
        num = num - remainder
        power = power + 1
        num = num / base
    return res

def short_decimal_to_other_base(num,base):
    res = 0
    power = 0
    num = num * (-1) if num < 0 else num
    while num > 0:
        res += (num % base)*(10**power)
        num -= num % base
        power += 1
        num /= base
    return res

print(long_decimal_to_other_base(174,5))
print(short_decimal_to_other_base(174,5))