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


def long_str_list_bubble_sort(my_str, exclude_string, sep_char):
    str_list = []
    str_dic = {}
    cur_str = ""
    for cur_char in my_str:
        if cur_char == sep_char:
            if not cur_str in str_dic:  # Multiple if statements
                if cur_str != exclude_string:  # Multiple if statements
                    str_list.append(cur_str)
                    str_dic[cur_str] = True
            cur_str = ""
        else:
            cur_str = cur_str + cur_char  # Use of =
    if not cur_str in str_dic:  # Multiple if statements
        if cur_str != exclude_string:  # Multiple if statements
            str_list.append(cur_str)
    swapped = True
    while swapped:
        swapped = False
        run_length = len(str_list) - 1  # Temporary variable
        for i in range(run_length):
            first_str_char = str_list[i][-1]  # Temporary variable
            second_str_char = str_list[i + 1][-1]  # Temporary variable
            if first_str_char > second_str_char:
                swapped = True
                tmp = str_list[i]
                str_list[i] = str_list[i + 1]
                str_list[i + 1] = tmp

    return str_list


def short_str_list_bubble_sort(my_str, exclude_string, sep_char):
    str_list = []
    unique_list = []
    assert not len(my_str) or len(my_str) and my_str[-1] != ","
    if my_str:
        str_list = [""]
    for cur_char in my_str:
        if cur_char == sep_char:
            str_list.append("")
        else:
            str_list[-1] += cur_char  # Single line condition
    for cur_str in str_list:
        if str_list != exclude_string and cur_str not in unique_list:
            unique_list.append(cur_str)

    for i in range(len(unique_list) - 1):  # Single line computation
        for j in range(0, len(unique_list) - i - 1):
            if unique_list[j][-1] > unique_list[j + 1][-1]:  # Single line computation
                unique_list[j], unique_list[j + 1] = unique_list[j + 1], unique_list[j]

    return unique_list


my_str = "without,hello,cruel,miau,my,world,cruel,a,begin,hello,miau"
exclude_string = "miau"
sep_char = ","

print(long_str_list_bubble_sort(my_str, exclude_string, sep_char))
print(short_str_list_bubble_sort(my_str, exclude_string, sep_char))
