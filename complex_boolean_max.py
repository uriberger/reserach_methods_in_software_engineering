''' This function receives three lists: search_list, include_list, exclude_list, and an integer
"num". It returns the maximum negative value in search_list which is included in include_list and
is not divisible by num, or not included in exclude_list and is divisible by num, or minus infinity
if such a number doesn't exist.

Features tested:
- Multiple if statements vs. complex boolean expression
'''

import math

def long_complex_boolean_max(search_list, include_list, exclude_list, num):
    largest = (-1)*math.inf
    for x in search_list:
        if x > largest: # Multiple if statements
            if x < 0:
                if x in include_list:
                    if not x % num == 0:
                        largest = x
                if x not in exclude_list:
                    if x % num == 0:
                        largest = x
            
    return largest

def short_complex_boolean_max(search_list, include_list, exclude_list, num):
    largest = (-1)*math.inf
    for x in search_list:
        if ((x in include_list and not x % num == 0) or (x not in exclude_list and x % num == 0)) and x < 0 and x > largest: # Complex boolean expression
            largest = x
            
    return largest

a = [-54,76,-32,-87,44,0,-9,-16]
b = [3,-60,25,-16,-12]
c = [6,-50,66,-25,-16]

# Both should be -32
print(long_complex_boolean_max(a,b,c,4))
print(short_complex_boolean_max(a,b,c,4))
# Both should be minus infinity
print(long_complex_boolean_max(a,[-14,-21,-49],c,7))
print(short_complex_boolean_max(a,[-14,-21,-49],c,7))