from itertools import combinations
def solution(numbers):
    comb = list(combinations(numbers, 2))
    answer = []
    for i in comb:
        answer.append(sum(i))
    answer = list(set(answer))
    answer = sorted(answer)
    return answer