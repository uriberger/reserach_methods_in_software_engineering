""" The purpose of this function is to create a copy of str1, where after every occurrence of
my_char we insert a copy of str2, unless we exceeded the maximum number of insertions.

Features tested:
- Multiple if statements vs. complex boolean expression
- Use of compound assignment operators vs. use of =
- Use of temporary variables vs. single line computation
"""


def long_str_insertion(str1, str2, my_char, max_insert_count):
    prev_ind = 0
    insert_count = 0
    res = ""
    for cur_ind in range(len(str1)):
        cur_char = str1[cur_ind]  # Temporary variable
        if cur_char == my_char:  # Multiple if statements
            if insert_count < max_insert_count:
                res = res + str1[prev_ind : cur_ind + 1]  # Use of =
                insert_count = insert_count + 1  # Use of =
                res = res + str2  # Use of =
                prev_ind = cur_ind + 1
    res = res + str1[prev_ind: cur_ind + 1]

    return res


def short_str_insertion(str1, str2, my_char, max_insert_count):
    prev_ind = insert_count = 0  # One line assignment
    res = ""
    for cur_ind in range(len(str1)):
        if (
            str1[cur_ind] == my_char and insert_count < max_insert_count
        ):  # Complex boolean expression, single line computation
            insert_count += 1  # Use of a compound assignment operator
            res += str1[prev_ind: cur_ind + 1] + str2  # Use of a compound assignment operator
            prev_ind = cur_ind + 1
    res += str1[prev_ind: cur_ind + 1]
    return res


str1 = "abtacadaetafag"
str2 = "z"
my_char = "a"
max_insert_count = 3

print(long_str_insertion(str1, str2, my_char, max_insert_count))
print(short_str_insertion(str1, str2, my_char, max_insert_count))
