def sort_list(unsorted_list: list[int]) -> list[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    """
    Selection Sort O(n^2) 
    Outer loop: Runs ones for each unsorted index, defining the total inner loops
    Inner loop: Pass ansorted list, find min value location, and swaps min with first
    unsorted element
    """
    for i in range(len(unsorted_list) -1):
        min = i
        for j in range(i+1, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[min]:
                min = j
        unsorted_list[i], unsorted_list[min] = unsorted_list[min], unsorted_list[i]
    return unsorted_list

if __name__ == "__main__":
    unsorted_list = [int(x) for x in input().split()]
    res = sort_list(unsorted_list)
    print(" ".join(map(str, res)))