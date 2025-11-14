def sort_list(unsorted_list: list[int]) -> list[int]:
    # Stable buble sort
    for j in range(len(unsorted_list)): # Loop through entire list 
        for i in range(len(unsorted_list) -1 -j):
            # Loop through list-1 -total iterations (to avoid compairing sorted elements)
            if unsorted_list[i] > unsorted_list[i+1]: # If not sorted, sort elements
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]
    return unsorted_list

if __name__ == "__main__":
    unsorted_list = [int(x) for x in input().split()]
    res = sort_list(unsorted_list)
    print(" ".join(map(str, res)))
