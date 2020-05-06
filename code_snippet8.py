def long_code_snippet8(l1, l2, p1, p2):
    res_list = []
    assert len(l1) == len(l2) and len(l2) == len(p1) and len(p1) == len(p2)
    n = len(l1)
    for i in range(n):
        if l1[p1[i]] > l2[p2[i]]:
            max_term = l1[p1[i]]
        else:
            max_term = l2[p2[i]]
        res_list.append(max_term)
    return res_list


def short_code_snippet8(l1, l2, p1, p2):
    res_list = []
    assert len(l1) == len(l2) and len(l2) == len(p1) and len(p1) == len(p2)
    for i in range(len(list1)):
        max_term = l1[p1[i]] if l1[p1[i]] > l2[p2[i]] else l2[p2[i]]
        res_list.append(max_term)
    return res_list
