def long_code_snippet10(row_num, col_num, base):
    my_array = []
    for i in range(row_num):
        my_array.append([])
        for j in range(col_num):
            add_val = i*j
            add_val = add_val**2
            add_val = add_val % base
            add_val = add_val * (-1)
            my_array[-1].append(add_val)
            
    return my_array

def short_code_snippet10(row_num, col_num, base):
    my_array = []
    for i in range(row_num):
        my_array.append([])
        for j in range(col_num):
            add_val = (((i*j)**2) % base) * (-1)
            my_array[-1].append(add_val)
            
    return my_array