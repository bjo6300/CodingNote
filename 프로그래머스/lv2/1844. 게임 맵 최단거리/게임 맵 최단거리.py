from collections import deque

def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    graph = [[-1 for _ in range(len(maps[0]))]for _ in range(len(maps))]
    
    q = deque([(0,0)])
    graph[0][0] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0<= nx < len(maps) and 0<= ny < len(maps[0]) and maps[nx][ny] == 1:
                if graph[nx][ny] == -1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append([nx, ny])
    
    return graph[-1][-1]
    