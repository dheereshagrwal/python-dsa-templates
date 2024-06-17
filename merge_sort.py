def merge_sort(arr, l, r):
    if l >= r:
        return
    mid = (l + r) // 2
    merge_sort(arr, l, mid)
    merge_sort(arr, mid + 1, r)
    merge(arr, l, mid, r)


def merge(arr, l, mid, r):
    left_arr = arr[l : mid + 1]
    right_arr = arr[mid + 1 : r + 1]
    i = 0
    j = 0
    k = l
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


arr = [10, 3, 76, 34, 23, 32]
merge_sort(arr, 0, len(arr) - 1)
print(arr)
