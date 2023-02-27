def binary_search(arr, x):
    """
    Search for x in the sorted list arr using binary search algorithm
    Returns the index of x in arr if found, otherwise returns -1
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binary_search(arr, x, low, high):
    """
    Search for x in the sorted list arr using binary search algorithm
    Returns the index of x in arr if found, otherwise returns -1
    """
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
