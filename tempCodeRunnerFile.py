def find_boundary(arr: list[bool]) -> int:
    """An array of boolean values is divided into two sections: 
    The left section consists of all false, and the right section consists of all true. 
    Find the First True in a Sorted Boolean Array of the right section, i.e.,
    the index of the first true element. If there is no true element, return -1."""

    # Implementing binary search
    left, right = 0, len(arr)-1
    result = -1

    while(left <= right): # While list not exausted
        mid = (left + right)//2
        if arr[mid]: # If index pointing to true
            result = mid
            right = mid - 1 # Move right boundary to left
        else:
            left = mid + 1
    return result

if __name__ == "__main__":
    arr = [x == "true" for x in input().split()]
    res = find_boundary(arr)
    print(res)
