''' This function receives a decimal integer and returns a representation in another base.

Features tested:
- Use of if statement vs. use of ternary assignment
- Use of temporary variables vs. single line computation
- Use of compound assignment operators vs. use of =

Possible bug creations:
- "remainder = num % base" -> "remainder = num % 10"
- "cur_power_factor = 10**power" -> "cur_power_factor = 10*power"
- "cur_addition = remainder*cur_power_factor" -> "cur_addition = remainder**cur_power_factor"
'''

def long_decimal_to_other_base(num,base):
    res = 0
    power = 0
    if num < 0: # Use of if statement
        num = num * (-1)
    while num > 0:
        remainder = num % base # Temporary variable
        cur_power_factor = 10**power # Temporary variable
        cur_addition = remainder*cur_power_factor # Temporary variable
        res = res + cur_addition # Use of =
        num = num - remainder # Use of =
        power = power + 1 # Use of =
        num = num / base
    return res

def short_decimal_to_other_base(num,base):
    res = 0
    power = 0
    num = num * (-1) if num < 0 else num # Use of ternary assignment
    while num > 0:
        res += (num % base)*(10**power) # Single line computation, use of compound assignment operator
        num -= num % base # Use of compound assignment operator
        power += 1 # Use of compound assignment operator
        num /= base # Use of compound assignment operator
    return res

print(long_decimal_to_other_base(174,5))
print(short_decimal_to_other_base(174,5))