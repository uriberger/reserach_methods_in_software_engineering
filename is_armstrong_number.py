# Determine whether the given number is Armstrong number or not. A positive integer of n digits is called an Armstrong number of order n (order is number of digits)
# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ...


#Note: // turns the division to int
def is_armstrong_number_long(num):
    n_str = str(num)
    n = len(n_str)
    temp = num
    sum1 = 0
    while temp != 0:
        r = temp % 10
        power = r**n
        sum1 = sum1 + power
        temp = temp // 10
    result = sum1 == num
    return result


#Note: // turns the division to int
def is_armstrong_number_short(num):
    n = len(str(num))
    temp = num
    sum1 = 0
    while temp != 0:
        sum1 += (temp % 10)**n
        temp //= 10
    return sum1 == num


assert True == is_armstrong_number_long(1634) == is_armstrong_number_short(1634)
assert False == is_armstrong_number_long(120) == is_armstrong_number_short(120)
