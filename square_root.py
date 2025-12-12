def square_root(n: int) -> int:
    """
    Given an integer, find its square root without using 
    the built-in square root function. 
    Only return the integer part (truncate the decimals).
    O(logn) time complexity 
    """
    if n < 2:
        return n # Handles 0 and 1
    low, high = 1, n//2

    while (low <= high): # Search space still valid
        mid = (low + high) // 2
        if mid*mid == n:
            return mid
        elif mid*mid < n:
            low = mid + 1 # Move to right
        else: # mid * mid > n
            high = mid - 1
    return high # Is the floor squared

if __name__ == "__main__":
    n = int(input())
    res = square_root(n)
    print(res)
