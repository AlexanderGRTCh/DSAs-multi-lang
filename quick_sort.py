def quick_sort_helper(unsorted_list: list[int], start, end) -> None:
    """
    Quick Sort: Lomuto partition (in-place, recursive)

    Select bottom of current partition (index 'end') as pivot.
    Assign two pointers (Scanner, Boundary) pointing at 'start' (top) of partition.
    Scanner increments one step each time; Boundary moves only after a swap.
    When Scanner value < Pivot, swap elements at Scanner and Boundary, then increment Boundary.
    When Scanner reaches pivot-1, swap Pivot with Boundary (pivot moves to final position).
    Recursively sort left [start, boundary-1] and right [boundary+1, end] partitions 
    (excluding pivot that is boundary at this point).
    Base case: partition size <= 1 (start >= end) -> already sorted.
    """

    # Base case If list partition has 1 or less elements
    if start >= end:
        return
    
    pivot = end # Select botom of list partition as pivot
    boundary, scanner = start, start # Assing 2 pointers 

    while scanner <= end - 1: # While within bounds -1
        if unsorted_list[scanner] < unsorted_list[pivot]:
            unsorted_list[scanner], unsorted_list[boundary] = unsorted_list[boundary], unsorted_list[scanner]
            boundary += 1 # Increent Boundary
        scanner += 1 # Increment Scanner
    unsorted_list[pivot], unsorted_list[boundary] = unsorted_list[boundary], unsorted_list[pivot]

    # Recursive call of sublist exluding pivot (boundary)
    quick_sort_helper(unsorted_list, start, boundary-1 )
    quick_sort_helper(unsorted_list, boundary +1, end)


# Helper function
def quick_sort(unsorted_list: list[int]) -> list[int]:
    quick_sort_helper(unsorted_list, 0, len(unsorted_list) -1)
    return unsorted_list


if __name__ == "__main__":

    unsorted_list = [int(x) for x in input().split()]

    res = quick_sort(unsorted_list)

    print(" ".join(map(str, res)))