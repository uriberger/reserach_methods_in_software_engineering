def long_merge_sort(x):
    list_of_lists = []
    for i in range(len(x)):
        list_of_lists.append([x[i]])
    while len(list_of_lists) > 1:
        next_list_of_lists = []
        list_of_lists_idx = 0
        while list_of_lists_idx < len(list_of_lists):
            if list_of_lists_idx == len(list_of_lists) - 1:
                next_list_of_lists.append(list_of_lists[list_of_lists_idx])
            else:
                list1 = list_of_lists[list_of_lists_idx]
                list2 = list_of_lists[list_of_lists_idx+1]
                list1_idx = 0
                list2_idx = 0
                res_list = []
                while list1_idx < len(list1) and list2_idx < len(list2):
                    if list1[list1_idx] > list2[list2_idx]:
                        res_list.append(list2[list2_idx])
                        list2_idx = list2_idx + 1
                    else:
                        res_list.append(list1[list1_idx])
                        list1_idx = list1_idx + 1
                for i in range(list1_idx, len(list1)):
                    res_list.append(list1[i])
                for i in range(list2_idx, len(list2)):
                    res_list.append(list2[i])
                next_list_of_lists.append(res_list)
                list_of_lists_idx = list_of_lists_idx + 2
        list_of_lists = next_list_of_lists
    return list_of_lists

def short_merge_sort(x):
    list_of_lists = [[y] for y in x]
    while len(list_of_lists) > 1:
        next_list_of_lists = []
        list_of_lists_idx = 0
        while list_of_lists_idx < len(list_of_lists):
            if list_of_lists_idx == len(list_of_lists) - 1:
                next_list_of_lists.append(list_of_lists[list_of_lists_idx])
            else:
                list1 = list_of_lists[list_of_lists_idx]
                list2 = list_of_lists[list_of_lists_idx+1]
                list1_idx = 0
                list2_idx = 0
                res_list = []
                while list1_idx < len(list1) and list2_idx < len(list2):
                    if list1[list1_idx] > list2[list2_idx]:
                        res_list.append(list2[list2_idx])
                        list2_idx = list2_idx + 1
                    else:
                        res_list.append(list1[list1_idx])
                        list1_idx = list1_idx + 1
                for i in range(list1_idx, len(list1)):
                    res_list.append(list1[i])
                for i in range(list2_idx, len(list2)):
                    res_list.append(list2[i])
                next_list_of_lists.append(res_list)
                list_of_lists_idx = list_of_lists_idx + 2
        list_of_lists = next_list_of_lists
    return list_of_lists

print(short_merge_sort([5,2,8,3,7,3,6,5]))