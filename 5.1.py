def main():
    n = int(input())
    a = dict()
    for _ in range(n):
        command = input().split()
        if command[0] == 'add':
            a[command[1]] = command[2]
        elif command[0] == 'del':
            if a.get(command[1]) is not None:
                del a[command[1]]
        elif command[0] == 'find':
            print(a.get(command[1], 'not found'))


if __name__ == '__main__':
    main()
