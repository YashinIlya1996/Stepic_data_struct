import sys


def main():
    # sys.stdin = open('input_4.2.txt', 'rt')
    input = sys.stdin.readline
    n, e, d = map(int, input().split())
    parents = [i for i in range(n + 1)]
    ranks = [0 for _ in range(n + 1)]
    answer = 1

    def find(i):
        if i != parents[i]:
            parents[i] = find(parents[i])
        return parents[i]

    def union(i, j):
        i_id = find(i)
        j_id = find(j)
        if i_id != j_id:
            if ranks[i_id] > ranks[j_id]:
                parents[j_id] = i_id
            else:
                parents[i_id] = j_id
                if ranks[i_id] == ranks[j_id]:
                    ranks[j_id] += 1

    for _ in range(e):
        union(*map(int, input().split()))

    for _ in range(d):
        i, j = map(int, input().split())
        if find(i) == find(j):
            answer = 0
            break

    print(answer)
    sys.stdin.close()


if __name__ == '__main__':
    main()
