#!/bin/python3


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def translate(raw_keyword, message):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    keyword = dedupe(list(raw_keyword))
    n = len(keyword)
    keyword_sorted = keyword.copy()
    keyword_sorted.sort()
    possible = [i for i in alphabet if i not in keyword_sorted]
    arr = keyword + possible
    arr2 = [arr[i::n] for i in range(n)]
    arr3 = {i: j for i, j in zip(keyword, arr2)}
    cipher_alphabet = []
    for i in keyword_sorted:
        cipher_alphabet = cipher_alphabet + arr3[i]
    cipher = {c: l for c, l, in zip(cipher_alphabet, alphabet)}
    solved = []
    for s in message:
        if s == ' ':
            solved.append(' ')
        else:
            solved.append(cipher[s])
    solved = ''.join(solved)
    return solved


def main():
    t = int(input())
    for i in range(t):
        print(translate(input(), input()))


if __name__ == '__main__':
    main()
