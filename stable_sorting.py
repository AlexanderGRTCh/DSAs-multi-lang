def sort_list(unsorted_list: list[int]) -> list[int]:
    """ Stable buble sort:
    We will iterate throughout the list using nested loops
    Outer loop: number of passes throughout the list
    Inner loop: compair unsorted adjastent elements and swap if needed
    Inner loop bounds: len(list) - 1 - total_complete_passes
    as each complete iteration places the largest remaining element at the end"""
    for i in range(len(unsorted_list)):
        for j in range(len(unsorted_list) -1 -i):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = (unsorted_list[j+1], unsorted_list[j])

    return unsorted_list

if __name__ == "__main__":
    unsorted_list = [int(x) for x in input().split()]
    res = sort_list(unsorted_list)
    print(" ".join(map(str, res)))