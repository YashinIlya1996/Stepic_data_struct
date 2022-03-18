P = 1_000_000_007
X = 263


class HashTable:
    def __init__(self, m: int):
        self.m = m
        self.table = [list() for _ in range(m)]

    def add(self, s: str):
        hv = self.my_hash(s, self.m)
        if s not in self.table[hv]:
            self.table[hv].append(s)

    def _del(self, s: str):
        if s in self.table[self.my_hash(s, self.m)]:
            self.table[self.my_hash(s, self.m)].remove(s)

    def find(self, s: str):
        if s in self.table[self.my_hash(s, self.m)]:
            print('yes')
        else:
            print('no')

    def check(self, s: str):
        if not self.table[int(s)]:
            print()
        else:
            for el in reversed(self.table[int(s)]):
                print(el, end=' ')
            print()

    @staticmethod
    def my_hash(s: str, m: int):
        h = 0
        for i, c in enumerate(s):
            h += (ord(c) * (X ** i)) % P
        return h % P % m


def main():
    m = int(input())
    n = int(input())
    ht = HashTable(m)
    funcs = {'add': lambda s: ht.add(s),
             'del': lambda s: ht._del(s),
             'find': lambda s: ht.find(s),
             'check': lambda s: ht.check(s)}
    for _ in range(n):
        command, *args = input().split()
        funcs[command](*args)


if __name__ == '__main__':
    main()
