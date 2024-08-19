def merge_sort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) >> 1
    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    left_arr = arr[low : mid + 1]
    right_arr = arr[mid + 1 : high + 1]
    i = 0
    j = 0
    k = low
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    for i in range(i, len(left_arr)):
        arr[k] = left_arr[i]
        k += 1

    for j in range(j, len(right_arr)):
        arr[k] = right_arr[j]
        k += 1


arr = [10, 3, 76, 34, 23, 32]
merge_sort(arr, 0, len(arr) - 1)
print(arr)
