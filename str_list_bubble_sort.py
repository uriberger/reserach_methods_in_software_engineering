""" This function receives a string as input, and first separates it into substring separated by
sep_char. It creates a list of the substrings, including only substrings different than
exclude_string. It then sorts the list according to the last character.

Features tested:
- Multiple if statements vs. complex boolean expression
- Use of compound assignment operators vs. use of =
- Use of temporary variables vs. single line computation

Possible bug creations:
- "if len(cur_str) >= index:" -> "if cur_str >= index:"
"""


def long_str_list_bubble_sort(str_list):
    iterations_num = len(str_list) - 1
    for i in range(iterations_num):
        internal_iterations = len(str_list) - i - 1
        for j in range(0, internal_iterations):
            str1 = str_list[j]
            str2 = str_list[j+1]
            compare1 = str1[-1]
            compare2 = str2[-1]
            if compare1 > compare2:
                str_list[j] = str2
                str_list[j+1] = str1
    return str_list


def short_str_list_bubble_sort(str_list):
    for i in range(len(str_list) - 1):
        for j in range(0, len(str_list) - i - 1):
            if str_list[j][-1] > str_list[j + 1][-1]:
                str_list[j], str_list[j + 1] = str_list[j + 1], str_list[j]
    return str_list


my_str = "without,hello,cruel,miau,my,world,cruel,a,begin,hello,miau"
exclude_string = "miau"
sep_char = ","

print(long_str_list_bubble_sort(my_str, exclude_string, sep_char))
print(short_str_list_bubble_sort(my_str, exclude_string, sep_char))


