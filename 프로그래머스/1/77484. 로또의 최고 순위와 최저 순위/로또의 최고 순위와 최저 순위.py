def solution(lottos, win_nums):
    rank = {}
    rank[6] = 1
    rank[5] = 2
    rank[4] = 3
    rank[3] = 4
    rank[2] = 5
    rank[1] = 6
    rank[0] = 6
        
    answer = []
    winning = 0
    zero = lottos.count(0)
    for i in range(len(win_nums)):
        if lottos[i] in win_nums:
            winning += 1
    answer = [rank[winning + zero], rank[winning]]
    return answer