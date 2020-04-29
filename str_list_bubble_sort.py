''' This function receives a string as input, and first separates it into substring separated by
sep_char. It creates a list of the substrings, including only substrings not shorter than index, and
different than exclude_string. It then sorts the list according to the character at the given index.

Features tested:
- Multiple if statements vs. complex boolean expression
- Use of compound assignment operators vs. use of =
- Use of temporary variables vs. single line computation
'''

def long_str_list_bubble_sort(my_str,index,exclude_string,sep_char):
    str_list = []
    str_dic = {}
    cur_str = ''
    for cur_char in my_str:
        if cur_char == sep_char:
            if not cur_str in str_dic: # Multiple if statements
                if len(cur_str) >= index: # Multiple if statements
                    if cur_str != exclude_string: # Multiple if statements
                        str_list.append(cur_str)
                        str_dic[cur_str] = True
            cur_str = ''
        else:
            cur_str = cur_str + cur_char # Use of =
    if not cur_str in str_dic: # Multiple if statements
        if len(cur_str) >= index: # Multiple if statements
            if cur_str != exclude_string: # Multiple if statements
                str_list.append(cur_str)
    swapped = True
    while swapped:
        swapped = False
        run_length = len(str_list)-1 # Temporary variable
        for i in range(run_length):
            first_str_char = str_list[i][index] # Temporary variable
            second_str_char = str_list[i+1][index] # Temporary variable
            if first_str_char > second_str_char:
                swapped = True
                tmp = str_list[i]
                str_list[i] = str_list[i+1]
                str_list[i+1] = tmp
                
    return str_list

def short_str_list_bubble_sort(my_str,index,exclude_string,sep_char):
    str_list = []
    str_dic = {}
    cur_str = ''
    for cur_char in my_str:
        if cur_char == sep_char:
            if not cur_str in str_dic and len(cur_str) >= index and cur_str != exclude_string: # Complex boolean expression
                str_list.append(cur_str)
                str_dic[cur_str] = True
            cur_str = ''
        else:
            cur_str += cur_char # Use of a compound assignment operator
    if not cur_str in str_dic and len(cur_str) >= index and cur_str != exclude_string: # Complex boolean expression
        str_list.append(cur_str)
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(str_list)-1): # Single line computation
            if str_list[i][index] > str_list[i+1][index]: # Single line computation
                swapped = True
                tmp = str_list[i]
                str_list[i] = str_list[i+1]
                str_list[i+1] = tmp
                
    return str_list

my_str = 'without,hello,cruel,miau,my,world,cruel,a,begin,hello,miau'
index = 3
exclude_string = 'miau'
sep_char = ','

print(long_str_list_bubble_sort(my_str, index, exclude_string, sep_char))
print(short_str_list_bubble_sort(my_str, index, exclude_string, sep_char))