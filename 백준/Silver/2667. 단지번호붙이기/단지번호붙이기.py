# 단지 번호 

from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input().rstrip())
danji = []

def bfs(graph, a, b): # a, b는 좌표
    house = 1
    q = deque([(a, b)])
    graph[a][b] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = 0
                    house += 1
                    
    return house

graph = [list(map(int, input().rstrip())) for _ in range(N)] # 지도   

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            danji.append(bfs(graph, i, j))

danji.sort() # 오름차순 정렬

print(len(danji)) # 총 단지 수

for i in danji:
    print(i) # 단지 내 집의 수
