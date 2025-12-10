def first_not_smaller(arr: list[int], target: int) -> int:
    """Given an array of integers sorted in increasing order and a target, 
    find the index of the first element in the array that is larger than 
    or equal to the target. 
    Assume that it is guaranteed to find a satisfying number."""

    # Implimintation of binary search
    left, right = 0, len(arr)-1
    result = -1

    while(left <= right): # While search space not exhausted
        mid = (left + right) // 2
        if target > arr[mid]:
            left = mid + 1
        else: # target <= arr[mid]:
            result = mid
            right = mid - 1
    return result

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = first_not_smaller(arr, target)
    print(res)