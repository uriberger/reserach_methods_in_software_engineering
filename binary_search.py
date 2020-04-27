''' This function performs a binary search. '''

def long_binary_search(ordered_list, term):
    low_border = 0
    high_border = len(ordered_list)
    while high_border - low_border > 1:
        cur_len = high_border-low_border
        half_len = int(cur_len/2)
        center_location = low_border+half_len
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
        if term == ordered_list[low_border+int((high_border-low_border)/2)]:
            return True
        elif term < ordered_list[low_border+int((high_border-low_border)/2)]:
            high_border = low_border+int((high_border-low_border)/2)
        else:
            low_border = low_border+int((high_border-low_border)/2)
    return False

print(long_binary_search([1,2,3,5], 3))
print(short_binary_search([1,2,3,5], 3))
print(long_binary_search([1,2,3,5,9,12], 7))
print(short_binary_search([1,2,3,5,9,12], 7))