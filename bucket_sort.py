def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]

    # Insert elements into their respective buckets
    for i in arr:
        idx = int(n * i)
        buckets[idx].append(i)

    # Sort the elements of each bucket
    for i in range(n):
        buckets[i] = sorted(buckets[i])

    # Concatenate the sorted buckets
    k = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1


arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
bucket_sort(arr)
print(arr)
