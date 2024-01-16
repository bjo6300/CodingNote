from collections import deque
def solution(board, h, w):
    n = len(board)
    def bfs(a, b):
        q = deque()
        q.append((a, b))
        count = 0
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                
                if 0 <= nx < n and 0 <= ny < n:
                    if board[x][y] == board[nx][ny]:
                        count += 1
        return count
    
    return bfs(h, w)