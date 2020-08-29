import time
import timeit

GLOBAL_COUNT = 0

def merge_sort(list_to_sort):
    """
        check size to see if it can be split. This mentions the recursive end.
        split the list into left, right
        merge_sort(left), merge_sort(right)
        create a combined empty sorted list and pointers for the start of left and right
        move the pointers based on 
            if the value pointed by left is bigger add left and increment pointer
            else add right and increment right pointer
            if left or right pointer has reached the end, then you can append the entire alternative left or right list to the combined list.
        Do this inwards until you reach a bare minimum of 1 entry
        since you are splitting the list by half on each instance , time complexity is lg(n)
        Merging each splitted to one, is taking n time on worst case [each pointer is moving alternatively]. so total time complexity is n*lg(n)
    """
    if len(list_to_sort) < 2:
        return list_to_sort

    # doubt: in casse of odd split ?
    half = len(list_to_sort)//2
    left = merge_sort(list_to_sort[:half])
    right = merge_sort(list_to_sort[half:])

    sorted_list = []
    left_pointer = 0
    right_pointer = 0

    count = 0
    while len(sorted_list) < len(left) + len(right):
        # time.sleep(1)
        count += 1
        # Solution 2. This doesnst necessary become faster because extend itself is doing a loop inside.
        # if (left_pointer == len(left)):
        #     sorted_list.extend(right[right_pointer:])
        #     right_pointer = len(right)
        #     break
        
        # if (right_pointer == len(right)):
        #     sorted_list.extend(left[left_pointer:])
        #     left_pointer = len(left)
        #     break

        
        # if (left[left_pointer] < right[right_pointer]):
        #     sorted_list.append(left[left_pointer])
        #     left_pointer += 1
        # else:
        #     sorted_list.append(right[right_pointer])
        #     right_pointer += 1

        # Solution 1
        if (left_pointer < len(left)) and ((right_pointer == len(right)) or (left[left_pointer] < right[right_pointer])):
            sorted_list.append(left[left_pointer])
            left_pointer += 1
        else:
            sorted_list.append(right[right_pointer])
            right_pointer += 1
    global GLOBAL_COUNT
    GLOBAL_COUNT += count
    return sorted_list

if __name__ == '__main__':
    list_to_sort = [13, 12, 61, 24, 1, 19, 81, 40, 32]
    sorted_list = merge_sort(list_to_sort)
    print(sorted_list)
    print(GLOBAL_COUNT)