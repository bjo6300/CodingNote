import sys
input = sys.stdin.readline

def dfs(n, lst):
    if n == M: # M개를 뽑았다면
        answer.append(lst[:])
        return
    
    for i in range(1, N + 1):
        if not v[i] and (not lst or lst[-1] < i):
            # not v[i] : 선택하지 않은 숫자
            # not lst : 리스트 안에 없어야함 (1,1 / 2,2 방지)
            # lst[-1] < i : 오름차순 정렬
            v[i] = 1 # 방문 처리
            dfs(n + 1, lst + [i]) # lst에 방문한 i를 추가
            v[i] = 0 # 방문 처리 해제

N, M = map(int, input().split())

answer = []
v = [0] * (N + 1) # 중복 확인을 위한 배열

dfs(0, [])

for lst in answer:
    print(*lst)
