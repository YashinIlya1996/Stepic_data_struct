from sys import setrecursionlimit


def main():
    n = int(input())
    a = [el for el in map(int, input().split())]
    leafs = {i for i in range(n)}

    root = a.index(-1)
    heights = [0] * n
    heights[root] = 1

    def find_height_iter():
        for leaf in leafs:
            _leaf = leaf
            count = 1
            while _leaf != root:
                if not heights[_leaf]:
                    count += 1
                    _leaf = a[_leaf]
                else:
                    count += heights[_leaf] - 1
                    break
            _leaf = leaf
            while not (heights[_leaf] or _leaf == root):
                heights[_leaf] = count
                count -= 1
                _leaf = a[_leaf]

    find_height_iter()
    print(max(heights))


if __name__ == '__main__':
    main()
