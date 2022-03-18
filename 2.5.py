from collections import deque


def main():
    n = int(input())
    a = list(reversed(list(map(int, input().split()))))
    m = int(input())
    answer = []
    first, second = deque(), deque()

    def fill_second_from_a():
        maximum = -1
        for _ in range(m):
            if a:
                temp = a.pop()
                maximum = max(maximum, temp)
                second.append((temp, maximum))

    def fill_first_from_second():
        maximum = -1
        for _ in range(m):
            if second:
                temp = second.pop()
                maximum = max(maximum, temp[0])
                first.append((temp[0], maximum))

    fill_second_from_a()
    while second:
        if len(answer) == n - m + 1:
            break
        fill_first_from_second()
        second_maximum = -1
        answer.append(first.pop()[1])
        while first:
            if len(answer) == n - m + 1:
                break
            first_temp = first.pop()[1]
            try:
                second_temp = a.pop()
                second_maximum = max(second_maximum, second_temp)
                second.append((second_temp, second_maximum))
                answer.append(max(second_maximum, first_temp))
            except IndexError:
                pass
        try:
            second_temp = a.pop()
            second_maximum = max(second_maximum, second_temp)
            second.append((second_temp, second_maximum))
        except IndexError:
            pass

    print(*answer)


if __name__ == '__main__':
    # import sys
    # sys.stdin = open('input_2.5.txt', 'rt')
    main()
    # sys.stdin.close()



