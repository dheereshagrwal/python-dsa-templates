def count_sort(arr):
    mx = max(arr)
    n = len(arr)
    output = [0] * n
    count = [0] * (mx + 1)

    for i in range(n):
        count[arr[i]] += 1

    for i in range(1, mx + 1):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        count[arr[i]] -= 1
        output[count[arr[i]]] = arr[i]

    for i in range(n):
        arr[i] = output[i]


arr = [1, 2, 4, 3, 5, 6, 7, 8, 9, 10]
count_sort(arr)
print(arr)
