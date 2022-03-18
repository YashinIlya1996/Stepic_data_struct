from myheap import BinaryMinHeap0Based


def main():
    input()
    a = BinaryMinHeap0Based(list(map(int, input().split())))
    a.heapify()
    print(len(a.heapifyzer))
    for a, b in a.heapifyzer:
        print(a, b)


def test():
    import random
    a = BinaryMinHeap0Based([8, 5, 1, 5])
    a.heapify()
    for _ in range(10):
        print(a)
        print(a.extract_min())
        temp = random.randint(0, 15)
        print(temp)
        a.insert(temp)
        print(a.check_heap())


if __name__ == '__main__':
    main()
