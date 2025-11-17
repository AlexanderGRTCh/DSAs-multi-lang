def sort_list(unsorted_list: list[int]) -> list[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    """
    Outer loop: pick current element to insert in sorted left side list
    Inner loop: move left through sorted part, shifting bigger ellemnts to right
    until find the correct position.
    """
    for i in range(1, len(unsorted_list)):
        pivot = unsorted_list[i]
        j = i - 1
        while j >= 0 and pivot < unsorted_list[j]: # While pivot smaller to its left. Change pivot <= un_lst for unstable sort
            unsorted_list[j+1] = unsorted_list[j] # Move elements to right
            j -= 1
        unsorted_list[j+1] = pivot

    return unsorted_list
if __name__ == "__main__":
    unsorted_list = [int(x) for x in input().split()]
    res = sort_list(unsorted_list)
    print(" ".join(map(str, res)))