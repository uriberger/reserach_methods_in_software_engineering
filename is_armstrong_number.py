def is_armstrong_number_long(num):
    n_str = str(num)
    n = len(n_str)
    temp = num
    sum1 = 0
    while temp != 0:
        r = temp % 10
        sum1 = sum1 + r**n
        temp = temp / 10
    result = sum1 == num
    return result


def is_armstrong_number_short(num):
    n = len(str(num))
    temp = num
    sum1 = 0
    while temp != 0:
        sum1 += (temp % 10)**n
        temp /= 10
    return sum1 == num


