''' This function counts how many times each of the count characters appears in the corpus, and
returns the characters that appear more than 'threshold' times.

Features tested:
- List and dictionary comprehension vs. loops
- Use of compound assignment operators vs. use of =

Possible bug creations:
- "if count_dics[count_char] > threshold:" -> "if count_char > threshold:"
'''

def long_count_chars(corpus, count_chars, threshold):
    count_dics = {} # Use a loop to initialize the dictionary
    for count_char in count_chars:
        count_dics[count_char] = 0
    for cur_char in corpus:
        if cur_char in count_chars:
            count_dics[cur_char] = count_dics[cur_char] + 1 # Use of =
    res = []
    for count_char in count_chars: # Use of a loop to fill the list
        if count_dics[count_char] > threshold:
            res.append(count_char)
            
    return res

def short_count_chars(corpus, count_chars, threshold):
    count_dics = {count_char : 0 for count_char in count_chars} # Use dictionary comprehension to initialize the dictionary
    for cur_char in corpus:
        if cur_char in count_chars:
            count_dics[cur_char] += 1 # Use of compound assignment operator
    res = [count_char for count_char in count_chars if count_dics[count_char] > threshold] # Use of list comprehension to fill the list
            
    return res

corpus = 'Hey bob, please add a bit of sugar to this coffee'
count_chars = ['a','b','c','d']
threshold = 2

print(long_count_chars(corpus, count_chars, threshold))
print(short_count_chars(corpus, count_chars, threshold))