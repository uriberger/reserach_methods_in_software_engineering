""" This function receives two integers in 'base' representation, and returns the absolute value of
their difference (also in 'base' representation).

Features tested:
- Use of temporary variables vs. single line computation
- Multiple lines computation vs. single line computation
- Use of compound assignment operators vs. use of =
- Use of if statement vs. use of ternary assignment

Possible bug creations:
- "carry = carry + 1" -> "carry = carry + base"
- "diff = diff + base" -> "diff = diff + 1"
- "digit1 = num1 % 10" -> "digit1 = num1 / 10" (and same for digit2)
- "cur_power_factor = 10**power" -> "cur_power_factor = 10*power"

We chose "carry = carry + 1" -> "carry = carry + base"
"""

import math


def long_absolute_value_of_diff(num1, num2, base):
    orig_num1 = num1
    orig_num2 = num2
    res = 0
    power = 0
    carry = 0
    while num1 > 0 or num2 > 0:
        digit1 = num1 % 10  # Temporary variable
        digit2 = num2 % 10  # Temporary variable
        diff = digit1 - digit2  # Multiple lines computation
        diff = diff - carry  # Multiple lines computation
        carry = 0
        if diff < 0:
            carry = carry + 1  # Use of =
            diff = diff + base  # Use of =
        cur_power_factor = 10 ** power  # Temporary variable
        cur_addition = diff * cur_power_factor  # Temporary variable
        res = res + cur_addition  # Use of =

        power = power + 1  # Use of =

        frac_num1 = num1 / 10  # Temporary variable
        num1 = math.floor(frac_num1)
        frac_num2 = num2 / 10  # Temporary variable
        num2 = math.floor(frac_num2)
    if carry > 0:  # Use of if statement
        res = long_absolute_value_of_diff(orig_num2, orig_num1, base)

    return res


def short_absolute_value_of_diff(num1, num2, base):
    orig_num1 = num1
    orig_num2 = num2
    res = power = carry = 0  # One line assignment
    while num1 > 0 or num2 > 0:
        diff = (
            (num1 % 10) - (num2 % 10) - carry
        )  # No temporary variables, single line computation
        carry = 0
        if diff < 0:
            carry += 1  # Use of compound assignment operator
            diff += base  # Use of compound assignment operator
        res += diff * (
            10 ** power
        )  # No temporary variables, use of compound assignment operator
        power += 1  # Use of compound assignment operator

        num1 = math.floor(num1 / 10)  # No temporary variable
        num2 = math.floor(num2 / 10)  # No temporary variable
    res = (
        long_absolute_value_of_diff(orig_num2, orig_num1, base) if carry > 0 else res
    )  # Use of ternary assignment

    return res


print(long_absolute_value_of_diff(241, 302, 5))
print(short_absolute_value_of_diff(241, 302, 5))
