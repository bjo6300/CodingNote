import sys
input = sys.stdin.readline
from collections import deque

n = int(input().rstrip())
area = [list(map(int, input().rstrip().split())) for _ in range(n)] # 지역 리스트

visited = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(height, start_x, start_y):
    visited[start_x][start_y] = True
    q = deque()
    q.append((start_x, start_y))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4): # 동서남북 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and area[nx][ny] > height: # 높이보다 커서 물에 잠기지 않을 때
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    
max_height, min_height = 0, 101
cnt = 0 # 안전영역 개수

for i in range(n):
    for j in range(n):
        max_height = max(area[i][j], max_height)
        min_height = min(area[i][j], min_height)

for height in range(max_height):
    visited = [[0] * n for _ in range(n)]
    temp_cnt = 0

    for a in range(n):
        for b in range(n):
            if area[a][b] > height and not visited[a][b]:
                bfs(height, a, b)
                temp_cnt += 1 # height에 따른 안전영역 개수
    
    cnt = max(cnt, temp_cnt) # 안전영역 개수가 많은 것 저장

print(cnt)
    