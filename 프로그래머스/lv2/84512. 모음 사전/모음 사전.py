from itertools import product

def solution(word):
    lst = []

    for i in range(1, 6):
        for j in product(['A','E','I','O','U'], repeat = i):
            w = ''.join(j)
            lst.append(w)

    lst.sort()
    answer = lst.index(word) + 1

    return answer