class MinHeap:
    def __init__(self, data=[]):
        self.arr = data
        for i in range((len(self.arr) >> 1) - 1, -1, -1):
            self.heapify(i)

    def parent(self, i):
        return (i - 1) >> 1

    def left(self, i):
        return (i << 1) + 1

    def right(self, i):
        return (i << 1) + 2

    def insert(self, x):
        self.arr.append(x)
        i = len(self.arr) - 1
        while i > 0 and self.arr[self.parent(i)] > self.arr[i]:
            self.arr[i], self.arr[self.parent(i)] = (
                self.arr[self.parent(i)],
                self.arr[i],
            )
            i = self.parent(i)

    def extract_min(self):
        if not self.arr:
            raise IndexError("Heap is empty")
        min_val = self.arr[0]
        if len(self.arr) == 1:
            return self.arr.pop()
        last = self.arr.pop()
        self.arr[0] = last
        self.heapify(0)
        return min_val

    def delete(self, idx):
        if not self.arr:
            raise IndexError("Heap is empty")
        if idx < 0 or idx >= len(self.arr):
            raise IndexError("Index out of range")
        self.decrease_key(idx, float("-inf"))
        self.extract_min()

    def decrease_key(self, i, new_val):
        if i < 0 or i >= len(self.arr):
            raise IndexError("Index out of range")
        if new_val > self.arr[i]:
            raise ValueError("New value must be ≤ current value")
        self.arr[i] = new_val
        while i > 0 and self.arr[self.parent(i)] > self.arr[i]:
            self.arr[i], self.arr[self.parent(i)] = (
                self.arr[self.parent(i)],
                self.arr[i],
            )
            i = self.parent(i)

    def increase_key(self, i, new_val):
        if i < 0 or i >= len(self.arr):
            raise IndexError("Index out of range")
        if new_val < self.arr[i]:
            raise ValueError("New value must be ≥ current value")
        self.arr[i] = new_val
        self.heapify(i)

    def heapify(self, i):
        n = len(self.arr)

        while True:
            smallest = i
            l, r = self.left(i), self.right(i)
            if l < n and self.arr[l] < self.arr[smallest]:
                smallest = l
            if r < n and self.arr[r] < self.arr[smallest]:
                smallest = r
            if smallest == i:
                break
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            i = smallest

    # override string representation for easier debugging
    def __str__(self):
        return str(self.arr)


heap = MinHeap([3, 1, 4, 1, 5])
print(heap)  # Should be a valid min-heap, e.g., [1, 1, 4, 3, 5]
heap.insert(0)
print(heap)  # Should include 0 and maintain min-heap property
print(heap.extract_min())  # Should return 0
heap.decrease_key(2, 2)  # Assuming index 2 is valid
heap.increase_key(1, 10)
heap.delete(0)
