def long_code_snippet3(char_to_ind_dic):
    ind_to_char_dic = {}
    
    for key,val in char_to_ind_dic.items():
        for ind in val:
            if not ind in ind_to_char_dic:
                ind_to_char_dic[ind] = []
            ind_to_char_dic[ind].append(key)
            
    for char_list in ind_to_char_dic.values():
        assert(len(char_list) <= 1)
        
    key_list = list(ind_to_char_dic.keys())
    key_list.sort()
    res_str = ''
    for key in key_list:
        cur_char = ind_to_char_dic[key][0]
        res_str = res_str + cur_char
            
    return res_str

def short_code_snippet3(char_to_ind_dic):
    ind_to_char_dic = {val:[x for x in char_to_ind_dic.keys() if val in char_to_ind_dic[x]] for val in range(max([max(y) for y in char_to_ind_dic.values()])+1)}
    assert(max([len(x) for x in ind_to_char_dic.values()])==1)
    return "".join([x[0] for x in ind_to_char_dic.values()])