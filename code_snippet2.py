import math

def long_code_snippet2(ordered_list, term):
    low_border = 0
    high_border = len(ordered_list)
    while high_border - low_border > 1:
        cur_len = high_border-low_border
        half_len = math.floor(cur_len/2)
        center_location = low_border+half_len
        if term == ordered_list[center_location]:
            return True
        elif term < ordered_list[center_location]:
            high_border = center_location
        else:
            low_border = center_location
    return False
    
def short_code_snippet2(ordered_list, term):
    low_border = 0
    high_border = len(ordered_list)
    while high_border - low_border > 1:
        if term == ordered_list[low_border+math.floor((high_border-low_border)/2)]:
            return True
        elif term < ordered_list[low_border+math.floor((high_border-low_border)/2)]:
            high_border = low_border+math.floor((high_border-low_border)/2)
        else:
            low_border = low_border+math.floor((high_border-low_border)/2)
    return False