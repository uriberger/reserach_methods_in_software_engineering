def long_code_snippet12(my_str, index, exclude_string, sep_char):
    str_list = []
    str_dic = {}
    cur_str = ""
    for cur_char in my_str:
        if cur_char == sep_char:
            if not cur_str in str_dic:
                if len(cur_str) >= index:
                    if cur_str != exclude_string:
                        str_list.append(cur_str)
                        str_dic[cur_str] = True
            cur_str = ""
        else:
            cur_str = cur_str + cur_char
    if not cur_str in str_dic:
        if len(cur_str) >= index:
            if cur_str != exclude_string:
                str_list.append(cur_str)
    swapped = True
    while swapped:
        swapped = False
        run_length = len(str_list) - 1
        for i in range(run_length):
            first_str_char = str_list[i][index]
            second_str_char = str_list[i + 1][index]
            if first_str_char > second_str_char:
                swapped = True
                tmp = str_list[i]
                str_list[i] = str_list[i + 1]
                str_list[i + 1] = tmp

    return str_list


def short_code_snippet12(my_str, index, exclude_string, sep_char):
    str_list = []
    str_dic = {}
    cur_str = ""
    for cur_char in my_str:
        if cur_char == sep_char:
            if (
                not cur_str in str_dic
                and len(cur_str) >= index
                and cur_str != exclude_string
            ):
                str_list.append(cur_str)
                str_dic[cur_str] = True
            cur_str = ""
        else:
            cur_str += cur_char
    if not cur_str in str_dic and len(cur_str) >= index and cur_str != exclude_string:
        str_list.append(cur_str)
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(str_list) - 1):
            if str_list[i][index] > str_list[i + 1][index]:
                swapped = True
                tmp = str_list[i]
                str_list[i] = str_list[i + 1]
                str_list[i + 1] = tmp

    return str_list
