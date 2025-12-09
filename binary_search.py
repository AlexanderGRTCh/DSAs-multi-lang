def binary_search(arr: list[int], target: int) -> int:
    """Binary Search non-recursive"""
    
    left = 0
    right = len(arr)-1
    # While array is not exhausted
    while( right >= left):
        mid = (left + right)//2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = binary_search(arr, target)
    print(res)