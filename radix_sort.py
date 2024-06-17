def count_sort(arr, place):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        digit = (arr[i] // place) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (arr[i] // place) % 10
        count[digit] -= 1
        output[count[digit]] = arr[i]

    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    mx = max(arr)
    place = 1
    while mx // place:
        count_sort(arr, place)
        place *= 10
    return arr


arr = [222, 153, 20, 654, 751]
print(radix_sort(arr))
