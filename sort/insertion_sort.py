def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j = j - 1
    return arr

arr = [1, 2, 4, 3, 5, 6, 7, 8, 9, 10]
insertion_sort(arr)
print(arr)
