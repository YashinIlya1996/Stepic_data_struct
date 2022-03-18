from sys import stdin


def main():
    input = stdin.readline
    stack = []
    to_print = []
    query_count = int(input())
    default_max = 0
    for _ in range(query_count):
        s = input().split()
        command = s[0]
        if command == 'max':
            if stack:
                to_print.append(stack[-1])
            else:
                to_print.append(default_max)
        elif command == 'pop' and stack:
            stack.pop()
        else:
            value = int(s[1])
            if stack:
                if value > stack[-1]:
                    stack.append(value)
                else:
                    stack.append(stack[-1])
            else:
                stack.append(value)

    for el in to_print:
        print(el)


if __name__ == '__main__':
    main()
