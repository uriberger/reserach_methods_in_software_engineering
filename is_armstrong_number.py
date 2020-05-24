# Determine whether the given number is Armstrong number or not. A positive integer of n digits is called an Armstrong number of order n (order is number of digits)
# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ...

'''
Features tested:
- Temporary variable vs. a single line computation
- Use of compound assignment operators vs. use of =
'''

#Note: // turns the division to int
def is_armstrong_number_long(num):
    n_str = str(num) # Temporary variable
    n = len(n_str)
    temp = num
    sum1 = 0
    while temp != 0:
        r = temp % 10 # Temporary variable
        power = r**n # Temporary variable
        sum1 = sum1 + power # Use of =
        temp = temp // 10 # Use of =
    result = sum1 == num
    return result


#Note: // turns the division to int
def is_armstrong_number_short(num):
    n = len(str(num)) # Single line computation
    temp = num
    sum1 = 0
    while temp != 0:
        sum1 += (temp % 10)**n # Single line computation, use of a compound assignment operator
        temp //= 10 # Use of a compound assignment operator
    return sum1 == num


assert True == is_armstrong_number_long(1634) == is_armstrong_number_short(1634)
assert False == is_armstrong_number_long(120) == is_armstrong_number_short(120)
