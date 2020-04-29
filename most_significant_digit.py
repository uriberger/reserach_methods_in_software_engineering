''' This function receives a list as an input, an outputs the most significant digit for all the
numbers in the list which are in the range of (small_num,large_num) and are divisible by
include_factor and are not divisible by exclude_factor. The result should be in string form, with
commas separating the different digits.

Features tested:
- Multiple if statements vs. complex boolean expression
- Use of temporary variables vs. single line computation
- Use of compound assignment operators vs. use of =

Possible bug creations:
- Remove "most_significant_digit_int = math.floor(most_significant_digit_float)" (it should be an int, without this line it will be a float)
'''

import math

def long_most_significant_digit(my_list, large_num, small_num, include_factor, exclude_factor):
    res = ''
    first = True
    for cur_num in my_list:
        if cur_num < large_num: # Multiple if statements
            if cur_num > small_num:
                include_factor_remainder = cur_num % include_factor # Temporary variable
                if include_factor_remainder == 0:
                    exclude_factor_remainder = cur_num % exclude_factor # Temporary variable
                    if exclude_factor_remainder != 0:
                        ten_power = 1
                        while cur_num > ten_power:
                            ten_power = ten_power*10 # Use of =
                        ten_power = ten_power / 10 # Use of =
                        most_significant_digit_float = cur_num / ten_power # Temporary variable
                        most_significant_digit_int = math.floor(most_significant_digit_float) # Temporary variable
                        most_significant_digit_str = str(most_significant_digit_int) # Temporary variable
                        if first:
                            first = False
                        else:
                            res = res + ',' # Use of =
                        res = res + most_significant_digit_str # Use of =
    return res

def short_most_significant_digit(my_list, large_num, small_num, include_factor, exclude_factor):
    res = ''
    first = True
    for cur_num in my_list:
        if cur_num < large_num and cur_num > small_num and cur_num % include_factor == 0 and cur_num % exclude_factor != 0: # Single line computation, complex boolean expression
            ten_power = 1
            while cur_num > ten_power:
                ten_power *= 10 # Use of a compound assignment operator
            ten_power /= 10 # Use of a compound assignment operator
            if first:
                first = False
            else:
                res += ',' # Use of a compound assignment operator
            res += str(math.floor(cur_num / ten_power)) # Single line computation, use of a compound assignment operator
    return res

my_list = [180,190,734,660,22,2000]
large_num = 2000
small_num = 150
include_factor = 2
exclude_factor = 3

print(long_most_significant_digit(my_list, large_num, small_num, include_factor, exclude_factor))
print(short_most_significant_digit(my_list, large_num, small_num, include_factor, exclude_factor))