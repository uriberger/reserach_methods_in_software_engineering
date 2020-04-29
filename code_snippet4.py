import math

def long_code_snippet4(search_list, include_list, exclude_list, num):
    largest = (-1)*math.inf
    for x in search_list:
        if x > largest:
            if x < 0:
                if x in include_list:
                    if not x % num == 0:
                        largest = x
                if x not in exclude_list:
                    if x % num == 0:
                        largest = x
            
    return largest

def short_code_snippet4(search_list, include_list, exclude_list, num):
    largest = (-1)*math.inf
    for x in search_list:
        if ((x in include_list and not x % num == 0) or (x not in exclude_list and x % num == 0)) and x < 0 and x > largest:
            largest = x
            
    return largest