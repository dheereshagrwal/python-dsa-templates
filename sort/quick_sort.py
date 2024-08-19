def quick_sort(arr, low, high):
    if low >= high:
        return
    pivot_index = partition(arr, low, high)
    quick_sort(arr, low, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Pivot is the rightmost element
    i = low # Pointer for the greater element
    
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
            i += 1
    
    arr[i], arr[high] = arr[high], arr[i]  # Swap the pivot element with the element at i
    return i  # Return the partition point

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
