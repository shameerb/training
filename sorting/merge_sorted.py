def merge_sorted_n(lists):
    nos_of_list = len(lists)
    if nos_of_list < 2:
        return lists[0]
    elif nos_of_list == 2:
        return merge_sorted(lists[0], lists[1])
    else:
        split_c = nos_of_list//2
        left = lists[:split_c]
        right = lists[split_c:]
        left = merge_sorted_n(left)
        right = merge_sorted_n(right)
        return merge_sorted(left, right)

def merge_sorted(sorted_list1, sorted_list2):
    pointer1 = 0
    pointer2 = 0
    merged_list = []
    while len(merged_list) < (len(sorted_list1) + len(sorted_list2)):
        if pointer2 == len(sorted_list2) or (pointer1 != len(sorted_list1) and sorted_list1[pointer1] < sorted_list2[pointer2]):
            merged_list.append(sorted_list1[pointer1])
            pointer1 += 1
        else:
            merged_list.append(sorted_list2[pointer2])
            pointer2 += 1

    return merged_list


if __name__ == "__main__":
    my_list     = [3, 4, 6, 10, 11]
    alices_list = [1, 5, 8, 12, 14, 19]
    third_list = [2, 3, 4, 99]
    # print(merge_sorted(my_list, alices_list))
    # print(merge_sorted(my_list, alices_list))
    print(merge_sorted_n([my_list, alices_list, third_list]))