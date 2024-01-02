import sys
input = sys.stdin.readline
from collections import deque

n = int(input().rstrip())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

danzi = 0
answer = []

def bfs(a, b):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    house = 1
    graph[a][b] = 0

    q = deque()
    q.append((a,b))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = 0
                    house += 1

    answer.append(house)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i, j)
            danzi += 1

print(danzi)

answer.sort()

for i in answer:
    print(i)
