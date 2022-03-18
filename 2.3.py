def main():
    size, n = map(int, input().split())
    packages = []
    for _ in range(n):
        packages.append(tuple(map(int, input().split())))
    buffer = []
    end_time = 0
    for arrival, duration in packages:
        if buffer:
            while arrival >= buffer[0][1]:
                buffer.pop(0)
                if not buffer:
                    break

        if len(buffer) < size:
            begin_time = max(arrival, end_time)
            end_time = begin_time + duration
            buffer.append((begin_time, end_time))
            print(begin_time)

        else:
            print(-1)


if __name__ == '__main__':
    # import sys
    # sys.stdin = open('input_2.3.txt', 'rt')
    main()
    # sys.stdin.close()
