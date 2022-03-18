from random import randint

P = 1_000_000_007
X = randint(3, P - 1)
X_POW = []


def polynomial_hash(s: str):
    hash_value = 0
    for num, symbol in enumerate(s):
        hash_value += ord(symbol) * X_POW[num] % P
    return hash_value % P


def main():
    pattern = input()
    text = input()
    pattern_len = len(pattern)
    X_POW.append(1)
    for i in range(1, pattern_len):
        X_POW.append(X_POW[i - 1] * X % P)
    pattern_hash = polynomial_hash(pattern)
    text_hash = polynomial_hash(text[-pattern_len:])
    answer = []
    for i in range(len(text) - pattern_len, -1, -1):
        if text_hash == pattern_hash:
            if pattern == text[i: i + pattern_len]:
                answer.append(i)
        text_hash = ((text_hash - (ord(text[i + pattern_len - 1]) * X_POW[-1])) * X % P + ord(text[i - 1])) % P
    print(*reversed(answer))


def test():
    X = 12345
    pattern = input()
    text = input()
    X_POW.append(1)
    for i in range(1, len(pattern)):
        X_POW.append(X_POW[i - 1] * X % P)
    for i in range(len(text) - len(pattern) + 1):
        print(text[i: i+len(pattern)], ':', end=' ')
        print(polynomial_hash(text[i: i+len(pattern)]))
    print('----------------------------')
    text_hash = polynomial_hash(text[-len(pattern):])
    print(f'{text_hash = }')
    pattern_len = len(pattern)
    for i in range(len(text) - pattern_len - 1, -1, -1):
        text_hash = ((text_hash - (ord(text[i + pattern_len]) * X_POW[-1])) * X % P + ord(text[i])) % P
        print(f'{i = }; {text[i + pattern_len] = }; {text[i] = }; {text_hash = }')
    print('----------------------------')
    print(*X_POW)


if __name__ == '__main__':
    main()
