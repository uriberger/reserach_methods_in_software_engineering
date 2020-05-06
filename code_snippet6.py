def long_code_snippet6(num, base):
    res = 0
    power = 0
    if num < 0:
        num = num * (-1)
    while num > 0:
        remainder = num % base
        cur_power_factor = 10 ** power
        cur_addition = remainder * cur_power_factor
        res = res + cur_addition
        num = num - remainder
        power = power + 1
        num = num / base
    return res


def short_code_snippet6(num, base):
    res = 0
    power = 0
    num = -num if num < 0 else num  # abs
    while num > 0:
        res += (num % base) * (10 ** power)
        num -= num % base
        power += 1
        num /= base
    return res
