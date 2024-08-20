def count_sort(arr, place):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for num in arr:
        digit = (num // place) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for num in reversed(arr):
        digit = (num // place) % 10
        count[digit] -= 1
        output[count[digit]] = num

    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    mx = max(arr)
    place = 1
    while mx // place:
        count_sort(arr, place)
        place *= 10


arr = [222, 153, 20, 654, 751]
radix_sort(arr)
print(arr)
