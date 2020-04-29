''' This function creates a multidimensional array of the given dimensions, where the value in the
i,j cell is -(((iXj)^2) % base).

Features tested:
- Multiple lines computation vs. single line computation
'''

def long_multid_array(row_num, col_num, base):
    my_array = []
    for i in range(row_num):
        my_array.append([])
        for j in range(col_num):
            add_val = i*j # Multiple line computation
            add_val = add_val**2 # Multiple line computation
            add_val = add_val % base # Multiple line computation
            add_val = add_val * (-1) # Multiple line computation
            my_array[-1].append(add_val)
            
    return my_array

def short_multid_array(row_num, col_num, base):
    my_array = []
    for i in range(row_num):
        my_array.append([])
        for j in range(col_num):
            add_val = (((i*j)**2) % base) * (-1) # Single line computation
            my_array[-1].append(add_val)
            
    return my_array

row_num = 7
col_num = 3
base = 5

print(long_multid_array(row_num, col_num, base))
print(short_multid_array(row_num, col_num, base))