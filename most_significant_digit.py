'''This function receives a list as an input, an outputs the most significant digit for all the
numbers in the list which are in the range of (small_num,large_num) and are divisible by
include_factor and are not divisible by exclude_factor. The result should be in string form, with
commas separating the different digits. '''

import math

def long_most_significant_digit(my_list, large_num, small_num, include_factor, exclude_factor):
    res = ''
    first = True
    for cur_num in my_list:
        if cur_num < large_num:
            if cur_num > small_num:
                include_factor_remainder = cur_num % include_factor
                if include_factor_remainder == 0:
                    exclude_factor_remainder = cur_num % exclude_factor
                    if exclude_factor_remainder != 0:
                        ten_power = 1
                        while cur_num > ten_power:
                            ten_power = ten_power*10
                        ten_power = ten_power / 10
                        most_significant_digit_float = cur_num / ten_power
                        most_significant_digit_int = math.floor(most_significant_digit_float)
                        most_significant_digit_str = str(most_significant_digit_int)
                        if first:
                            first = False
                        else:
                            res = res + ','
                        res = res + most_significant_digit_str
    return res

def short_most_significant_digit(my_list, large_num, small_num, include_factor, exclude_factor):
    res = ''
    first = True
    for cur_num in my_list:
        if cur_num < large_num and cur_num > small_num and cur_num % include_factor == 0 and cur_num % exclude_factor != 0:
            ten_power = 1
            while cur_num > ten_power:
                ten_power *= 10
            ten_power /= 10
            if first:
                first = False
            else:
                res += ','
            res += str(math.floor(cur_num / ten_power))
    return res

my_list = [180,190,734,660,22,2000]
large_num = 2000
small_num = 150
include_factor = 2
exclude_factor = 3

print(long_most_significant_digit(my_list, large_num, small_num, include_factor, exclude_factor))
print(short_most_significant_digit(my_list, large_num, small_num, include_factor, exclude_factor))