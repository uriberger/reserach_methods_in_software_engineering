''' The purpose of this function is to create a copy of str1, where after every occurrence of
my_char we insert a copy of str2, unless the preceding character is escape_char or we exceeded the
maximum number of insertions. '''

def long_str_insertion(str1,str2,my_char,escape_char,max_insert_count):
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

def short_str_insertion(str1,str2,my_char,escape_char,max_insert_count):
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

str1 = 'abtacadaetafag'
str2 = 'z'
my_char = 'a'
escape_char = 't'
max_insert_count = 3

print(long_str_insertion(str1, str2, my_char, escape_char, max_insert_count))
print(short_str_insertion(str1, str2, my_char, escape_char, max_insert_count))