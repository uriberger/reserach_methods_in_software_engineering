import math


def long_code_snippet7(my_str, indices):
    best_start_index = -1
    smallest_gap = math.inf
    for start_index in indices:
        cur_smallest_gap = math.inf
        for end_index in indices:
            cur_gap = end_index - start_index
            if cur_gap > 0 and cur_gap < cur_smallest_gap:
                cur_smallest_gap = cur_gap
        if cur_smallest_gap < smallest_gap:
            best_start_index = start_index
            smallest_gap = cur_smallest_gap

    res = ""
    for i in range(best_start_index, best_start_index + smallest_gap):
        res = res + my_str[i]

    return res


def short_code_snippet7(my_str, indices):
    best_start_index = -1
    smallest_gap = math.inf
    for start_index in indices:
        cur_smallest_gap = math.inf
        for end_index in indices:
            if (
                end_index - start_index > 0
                and end_index - start_index < cur_smallest_gap
            ):
                cur_smallest_gap = end_index - start_index
        if cur_smallest_gap < smallest_gap:
            best_start_index = start_index
            smallest_gap = cur_smallest_gap

    return my_str[best_start_index : best_start_index + smallest_gap]
