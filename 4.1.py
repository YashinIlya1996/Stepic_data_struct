def main():
    import sys
    input = sys.stdin.readline
    tables_count, operations_count = map(int, input().split())
    tables = []
    current_max = -1
    for size in map(int, input().split()):
        tables.append([size])
        if size > current_max:
            current_max = size
    for _ in range(operations_count):
        destination, source = map(int, input().split())
        _d = destination - 1
        _s = source - 1

        def find_replace(i):
            if isinstance(tables[i], list):
                return i
            else:
                tables[i] = find_replace(tables[i])
                return tables[i]

        _d = find_replace(_d)
        _s = find_replace(_s)
        if _d != _s:
            tables[_d][0] += tables[_s][0]
            tables[_s] = _d
            if tables[_d][0] > current_max:
                current_max = tables[_d][0]
        print(current_max)


if __name__ == '__main__':
    main()
