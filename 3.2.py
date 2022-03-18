from myheap import BinaryMinHeap0Based


def main():
    n, m = map(int, input().split())
    tasks = list(map(int, input().split()))
    heap = BinaryMinHeap0Based([(0, i) for i in range(n)])
    for task in tasks:
        cur = heap.get_min
        print(cur[1], cur[0])
        heap.change_value(0, (cur[0] + task, cur[1]))


# import heapq
#
#
# def main():
#     n, m = map(int, input().split())
#     tasks = list(map(int, input().split()))
#     h = [(0, i) for i in range(n)]
#     heapq.heapify(h)
#     for task in tasks:
#         btime, proc = h[0]
#         heapq.heapreplace(h, (btime + task, proc))
#         print(proc, btime)


if __name__ == '__main__':
    main()