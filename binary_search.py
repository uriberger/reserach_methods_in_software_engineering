''' This function performs a binary search.

Features tested:
- Use of temporary variables vs. a single line computation

Possible bug creations:
- "center_location = low_border+half_len" -> "center_location = low_border+half_len+1"
- "half_len = math.floor(cur_len/2)" -> "half_len = cur_len/2"
- "center_location = low_border+half_len" -> "center_location = high_border+half_len"

We chose "center_location = low_border+half_len" -> "center_location = low_border+half_len+1"
'''

import math

def long_binary_search(ordered_list, term):
    low_border = 0
    high_border = len(ordered_list)
    while high_border - low_border > 1:
        cur_len = high_border-low_border # Temporary variable
        half_len = math.floor(cur_len/2) # Temporary variable
        center_location = low_border+half_len # Temporary variable
        if term == ordered_list[center_location]:
            return True
        elif term < ordered_list[center_location]:
            high_border = center_location
        else:
            low_border = center_location
    return False
    
def short_binary_search(ordered_list, term):
    low_border = 0
    high_border = len(ordered_list)
    while high_border - low_border > 1:
        if term == ordered_list[low_border+math.floor((high_border-low_border)/2)]: # No temporary variable
            return True
        elif term < ordered_list[low_border+math.floor((high_border-low_border)/2)]: # No temporary variable
            high_border = low_border+math.floor((high_border-low_border)/2) # No temporary variable
        else:
            low_border = low_border+math.floor((high_border-low_border)/2) # No temporary variable
    return False

print(long_binary_search([1,2,3,5], 3))
print(short_binary_search([1,2,3,5], 3))
print(long_binary_search([1,2,3,5,9,12], 7))
print(short_binary_search([1,2,3,5,9,12], 7))