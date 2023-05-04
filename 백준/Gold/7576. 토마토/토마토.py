import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

def bfs():
    while q:
        a, b = q.popleft()

        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b
            
            if 0<= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0: # 0은 흰색이므로 침투가능
                    graph[nx][ny] = graph[a][b] + 1
                    q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))

bfs()

result = -2
flag = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            flag = 1
        else:
            result = max(result, graph[i][j])

if flag == 1:
    print(-1)
elif result == 1:
    print(0)
else:
    print(result - 1)