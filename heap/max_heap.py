class MaxHeap:
    def __init__(self, data=[]):
        self.arr = data.copy()
        self.n = len(self.arr)
        for i in range((self.n >> 1) - 1, -1, -1):
            self.heapify(i, self.n)

    def parent(self, i):
        return (i - 1) >> 1

    def left(self, i):
        return (i << 1) + 1

    def right(self, i):
        return (i << 1) + 2

    def heapify(self, i, n):
        while True:
            largest = i
            l, r = self.left(i), self.right(i)
            if l < n and self.arr[l] > self.arr[largest]:
                largest = l
            if r < n and self.arr[r] > self.arr[largest]:
                largest = r
            if largest == i:
                break
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            i = largest

    def insert(self, x):
        self.arr.append(x)
        i = self.n
        self.n += 1
        while i > 0 and self.arr[i] > self.arr[self.parent(i)]:
            self.arr[i], self.arr[self.parent(i)] = (
                self.arr[self.parent(i)],
                self.arr[i],
            )
            i = self.parent(i)

    def extract_max(self):
        if not self.arr:
            raise IndexError("Heap is empty")
        max_val = self.arr[0]
        if self.n == 1:
            self.n -= 1
            return self.arr.pop()
        last = self.arr.pop()
        self.n -= 1
        self.arr[0] = last
        self.heapify(0, self.n)
        return max_val

    def increase_key(self, i, new_val):
        if i < 0 or i >= self.n:
            raise IndexError("Index out of range")
        if new_val < self.arr[i]:
            raise ValueError("New value must be ≥ current value")
        self.arr[i] = new_val
        while i > 0 and self.arr[i] > self.arr[self.parent(i)]:
            self.arr[i], self.arr[self.parent(i)] = (
                self.arr[self.parent(i)],
                self.arr[i],
            )
            i = self.parent(i)

    def delete(self, idx):
        if not self.arr:
            raise IndexError("Heap is empty")
        if idx < 0 or idx >= self.n:
            raise IndexError("Index out of range")
        self.increase_key(idx, float("inf"))
        self.extract_max()

    def decrease_key(self, i, new_val):
        if i < 0 or i >= self.n:
            raise IndexError("Index out of range")
        if new_val > self.arr[i]:
            raise ValueError("New value must be ≤ current value")
        self.arr[i] = new_val
        self.heapify(i, self.n)

    def sort(self):
        for i in range(self.n - 1, 0, -1):
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
            self.heapify(0, i)

    def __str__(self):
        return str(self.arr)
        