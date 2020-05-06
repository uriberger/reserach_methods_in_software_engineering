""" This function receives a string and a list of indices in the string as an input, and outputs
ad substring of the 2 subsequent indices with the smallest gap.

Features tested:
- Using a loop vs. string slicing
- Temporary variable vs. a single line computation
"""

import math


def long_extract_substring(my_str, indices):
    best_start_index = -1
    smallest_gap = math.inf
    for start_index in indices:
        cur_smallest_gap = math.inf
        for end_index in indices:
            cur_gap = end_index - start_index  # Temporary variable
            if cur_gap > 0 and cur_gap < cur_smallest_gap:
                cur_smallest_gap = cur_gap
        if cur_smallest_gap < smallest_gap:
            best_start_index = start_index
            smallest_gap = cur_smallest_gap

    res = ""
    for i in range(best_start_index, best_start_index + smallest_gap):  # Use a loop
        res = res + my_str[i]

    return res


def short_extract_substring(my_str, indices):
    best_start_index = -1
    smallest_gap = math.inf
    for start_index in indices:
        cur_smallest_gap = math.inf
        for end_index in indices:
            if (
                end_index - start_index > 0
                and end_index - start_index < cur_smallest_gap
            ):  # A single line computation
                cur_smallest_gap = end_index - start_index  # A single line copmutation
        if cur_smallest_gap < smallest_gap:
            best_start_index = start_index
            smallest_gap = cur_smallest_gap

    return my_str[
        best_start_index: best_start_index + smallest_gap
    ]  # Use string slicing


my_str = "abcdefghijklmnopqrstuvwxyz"
indices = [8, 22, 11, 2, 0, 5, 15, 18, 25]

print(long_extract_substring(my_str, indices))
print(short_extract_substring(my_str, indices))
