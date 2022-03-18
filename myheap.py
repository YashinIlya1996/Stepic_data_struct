class BinaryMinHeap0Based:
    def __init__(self, lst, log=False):
        self.heap = list(lst)
        self.heapifyzer = []
        self.log = log

    @property
    def size(self):
        return len(self.heap)

    def left_child(self, i):
        return 2 * i + 1 if 2 * i + 1 <= self.size - 1 else None

    def right_child(self, i):
        return 2 * i + 2 if 2 * i + 2 <= self.size - 1 else None

    def parent(self, i):
        return (i - 1) // 2 if 0 < i <= self.size else None

    def _swap(self, ip, ich):
        try:
            self.heap[ip], self.heap[ich] = self.heap[ich], self.heap[ip]
            if self.log: self.heapifyzer.append((ip, ich))
        except IndexError:
            pass

    def sift_up(self, i):
        while self.parent(i) is not None and self.heap[i] < self.heap[self.parent(i)]:
            self._swap(self.parent(i), i)
            i = self.parent(i)

    def sift_down(self, i):
        min_index = i
        while True:
            if self.right_child(i) is not None and self.heap[self.right_child(i)] < self.heap[i]:
                min_index = self.right_child(i)
            if self.left_child(i) is not None and self.heap[self.left_child(i)] < self.heap[min_index]:
                min_index = self.left_child(i)
            if min_index == i:
                break
            self._swap(i, min_index)
            i = min_index

    @property
    def get_min(self):
        return self.heap[0] if self.heap else None

    def insert(self, value):
        self.heap.append(value)
        self.sift_up(self.size - 1)

    def extract_min(self):
        try:
            result = self.heap[0]
            if self.size > 1:
                self.heap[0] = self.heap.pop()
                self.sift_down(0)
            else:
                self.heap.pop()
        except IndexError:
            result = None
        return result

    def remove(self, i):
        self.heap[i] = -float('inf')
        self.sift_up(i)
        self.extract_min()

    def change_value(self, i, value):
        old_value = self.heap[i]
        self.heap[i] = value
        if old_value < value:
            self.sift_down(i)
        else:
            self.sift_up(i)

    def check_heap(self):
        for i in range((self.size - 1) // 2):
            if self.left_child(i) is not None:
                if self.heap[self.left_child(i)] < self.heap[i]:
                    return False
            if self.right_child(i) is not None:
                if self.heap[self.right_child(i)] < self.heap[i]:
                    return False
        return True

    def heapify(self):
        for i in range((self.size - 1) // 2, -1, -1):
            self.sift_down(i)

    def __repr__(self):
        return list.__repr__(self.heap)
