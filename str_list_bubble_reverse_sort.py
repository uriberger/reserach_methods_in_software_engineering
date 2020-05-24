""" This function receives a list of strings as input, and sorts the list according to the reversed
string.

Features tested:
- Use of temporary variables vs. single line computation
- Values switch using temporary variable vs. multiple assignment
"""

def long_str_list_bubble_sort(str_list):
    iterations_num = len(str_list) - 1 # Temporary variable
    for i in range(iterations_num):
        internal_iterations = len(str_list) - i - 1 # Temporary variable
        for j in range(0, internal_iterations):
            str1 = str_list[j] # Temporary variable
            str2 = str_list[j+1] # Temporary variable
            compare1 = str1[::-1] # Temporary variable
            compare2 = str2[::-1] # Temporary variable
            if compare1 > compare2:
                str_list[j] = str2 # Values switch using a temporary variable
                str_list[j+1] = str1 # Values switch using a temporary variable
    return str_list


def short_str_list_bubble_sort(str_list):
    for i in range(len(str_list) - 1): # Single line computation
        for j in range(0, len(str_list) - i - 1): # Single line computation
            if str_list[j][::-1] > str_list[j + 1][::-1]: # Single line computation
                str_list[j], str_list[j + 1] = str_list[j + 1], str_list[j] # Values switch using multiple assignment
    return str_list


str_list = ["without","hello","cruel","miau","my","world","crual","a","begin","hello","miau"]

print(long_str_list_bubble_sort(str_list))
print(short_str_list_bubble_sort(str_list))