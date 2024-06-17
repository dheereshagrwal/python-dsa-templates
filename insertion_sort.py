def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [1, 2, 4, 3, 5, 6, 7, 8, 9, 10]
insertion_sort(arr)
print(arr)
