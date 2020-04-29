def long_code_snippet11(str1,str2,my_char,escape_char,max_insert_count):
    prev_ind = 0
    prev_char = None
    insert_count = 0
    res = ''
    for cur_ind in range(len(str1)):
        cur_char = str1[cur_ind]
        if cur_char == my_char:
            if prev_char != escape_char:
                if insert_count < max_insert_count:
                    res = res + str1[prev_ind:cur_ind+1]
                    insert_count = insert_count + 1
                    for _ in range(insert_count):
                        res = res + str2
                    prev_ind = cur_ind+1
        prev_char = cur_char
    res = res + str1[prev_ind:cur_ind+1]
    
    return res

def short_code_snippet11(str1,str2,my_char,escape_char,max_insert_count):
    prev_ind = 0
    prev_char = None
    insert_count = 0
    res = ''
    for cur_ind in range(len(str1)):
        if str1[cur_ind] == my_char and prev_char != escape_char and insert_count < max_insert_count:
            res += str1[prev_ind:cur_ind+1]
            insert_count += 1
            res += insert_count*str2
            prev_ind = cur_ind + 1
        prev_char = str1[cur_ind]
    res += str1[prev_ind:cur_ind+1]
    
    return res