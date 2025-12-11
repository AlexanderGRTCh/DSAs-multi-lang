def find_first_occurrence(arr: list[int], target: int) -> int:
    """Given a sorted array of integers and a target integer, 
    find the first occurrence of the target and return its index. 
    Return -1 if the target is not in the array.
    Most efficient approach: Binary Search O(nlogn) time complexity."""

    if len(arr) <= 0:
        return -1
    left, right = 0, len(arr)-1 # Initiate pointers at begin/end of array

    while(left <= right): # While array not exhausted
        mid = (left + right)//2 # Points midle of list rounded down
        
        if(arr[mid] < target):
            left = mid + 1 # Move right
        else: # arr[mid] >= target
            right = mid - 1 # Move left
    return left if left < len(arr) and arr[left] == target else -1

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = find_first_occurrence(arr, target)
    print(res)