def merge_ranges(n):
    sorted_arr = sorted(n)
    merged = sorted_arr[0]
    for current_start, current_end in sorted_arr[1:]:
        previous_start, previous_end = merged[-1]
        if (current_start <= previous_end):
            merged[-1] = (previous_start, max(current_end, previous_end))
        else:
            merged.append((current_start, current_end))
    return merged

if __name__ == '__main__':
    n = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    merged = merge_ranges(n)
    print(merged)