def sort_list(unsorted_list: list[int]) -> list[int]:
    """
    Recursively split list into single-element sublists;
    merge sublists compairing front elements;
    build and return coomplete ascending-order list.
    """

    ln = len(unsorted_list)
    # Base case
    if ln <= 1:
        return unsorted_list
    
    mid_point = ln // 2
    left_list = sort_list(unsorted_list[: mid_point])
    right_list = sort_list(unsorted_list[mid_point :])

    sorted_list = [] # Empy list to populate
    left_index, right_index = 0, 0 # Sub lists indexes

    # Merge sublists while either sublist has elements
    while left_index < mid_point or right_index < ln - mid_point:
        if left_index == mid_point: # If left_list is empty (iterated through)
            sorted_list.append(right_list[right_index]) # Append top element from right list
            right_index += 1 # Increment right pointer
        elif right_index == ln - mid_point: # If right_list is empty (iterated through)
            sorted_list.append(left_list[left_index])
            left_index += 1
        elif left_list[left_index] <= right_list[right_index]: # If top left list <= top right_list (For unstable use < instead)
            sorted_list.append(left_list[left_index])
            left_index += 1
        else: # Else top right list >= top left_list
            sorted_list.append(right_list[right_index])
            right_index += 1
    return sorted_list


if __name__ == "__main__":
    unsorted_list = [int(x) for x in input().split()]
    res = sort_list(unsorted_list)
    print(" ".join(map(str, res)))