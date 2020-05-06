""" The function receives a mapping of char->list of indices. It should build the implied string.
For example: if the input is:

'g' -> [2]
'd' -> [0]
'o' -> [1]

The output should be 'dog'.

Features tested:
- List and dictionary comprehension vs. loops
"""


def long_char_ind_to_str(char_to_ind_dic):
    ind_to_char_dic = {}

    for key, val in char_to_ind_dic.items():
        for ind in val:
            if not ind in ind_to_char_dic:
                ind_to_char_dic[ind] = []
            ind_to_char_dic[ind].append(key)

    for char_list in ind_to_char_dic.values():
        assert len(char_list) <= 1

    key_list = list(ind_to_char_dic.keys())
    key_list.sort()
    res_str = ""
    for key in key_list:
        cur_char = ind_to_char_dic[key][0]
        res_str = res_str + cur_char

    return res_str


def short_char_ind_to_str(char_to_ind_dic):
    ind_to_char_dic = {
        val: [x for x in char_to_ind_dic.keys() if val in char_to_ind_dic[x]]
        for val in range(max([max(y) for y in char_to_ind_dic.values()]) + 1)
    }
    assert max([len(x) for x in ind_to_char_dic.values()]) == 1
    return "".join([x[0] for x in ind_to_char_dic.values()])


# example_dic = {'a' : [0,4], 'v' : [1,4], 'o' : [2,6], 'c' : [3], 'd' : [5]}
example_dic = {"a": [0, 4], "v": [1], "o": [2, 6], "c": [3], "d": [5]}
print(short_char_ind_to_str(example_dic))
print(long_char_ind_to_str(example_dic))
