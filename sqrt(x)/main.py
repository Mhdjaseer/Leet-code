def mySqrt(x):
    if x == 0:
        return 0
    
    low, high = 1, x
    while low <= high:
        mid = low + (high - low) // 2
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            low = mid + 1
        else:
            high = mid - 1
    
    return high  # When the loop ends, high is the floor of the square root

# Example usage:
print(mySqrt(4))  # Output: 2
print(mySqrt(8))  # Output: 2
