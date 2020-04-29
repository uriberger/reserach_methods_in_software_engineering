def long_code_snippet5(corpus, count_chars, threshold):
    count_dics = {}
    for count_char in count_chars:
        count_dics[count_char] = 0
    for cur_char in corpus:
        if cur_char in count_chars:
            count_dics[cur_char] = count_dics[cur_char] + 1
    res = []
    for count_char in count_chars:
        if count_dics[count_char] > threshold:
            res.append(count_char)
            
    return res

def short_code_snippet5(corpus, count_chars, threshold):
    count_dics = {count_char : 0 for count_char in count_chars}
    for cur_char in corpus:
        if cur_char in count_chars:
            count_dics[cur_char] += 1
    res = [count_char for count_char in count_chars if count_dics[count_char] > threshold]
            
    return res