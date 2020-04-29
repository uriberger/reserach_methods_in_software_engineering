''' This function receives 2 lists (l1, l2) and too permutations (p1, p2) all of the same length
(n), and returns a list of size n so that the i'th term is the maximum between l1[p1[i]] and
l2[p2[i]].

Features tested:
- Use of temporary variables vs. single line computation
- Use of if statement vs. use of ternary assignment

Possible bug creations:
- Replace all "l1[p1[i]]" to "l1[i]" and all "l2[p2[i]]" to "l2[i]"
'''

def long_max_list(l1,l2,p1,p2):
    res_list = []
    assert(len(l1)==len(l2) and len(l2)==len(p1) and len(p1)==len(p2))
    n = len(l1) # Temporary variable
    for i in range(n):
        if l1[p1[i]] > l2[p2[i]]: # Use of if statement
            max_term = l1[p1[i]]
        else:
            max_term = l2[p2[i]]
        res_list.append(max_term)
    return res_list

def short_max_list(l1,l2,p1,p2):
    res_list = []
    assert(len(l1)==len(l2) and len(l2)==len(p1) and len(p1)==len(p2))
    for i in range(len(list1)): # Single line computation
        max_term = l1[p1[i]] if l1[p1[i]] > l2[p2[i]] else l2[p2[i]] # Use of ternary assignment
        res_list.append(max_term)
    return res_list

def very_short_max_list(l1,l2,p1,p2):
    res_list = []
    assert(len(l1)==len(l2) and len(l2)==len(p1) and len(p1)==len(p2))
    return [l1[p1[i]] if l1[p1[i]] > l2[p2[i]] else l2[p2[i]] for i in range(len(l1))]

list1 = [7,2,4,1,9,5]
list2 = [2,8,5,8,4,5]
perm1 = [2,4,5,3,1,0]
perm2 = [1,2,3,0,5,4]
print(long_max_list(list1, list2,perm1,perm2))
print(short_max_list(list1, list2,perm1,perm2))
print(very_short_max_list(list1, list2,perm1,perm2))