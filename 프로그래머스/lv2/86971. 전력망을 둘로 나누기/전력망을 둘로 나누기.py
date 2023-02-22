from collections import deque
def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    answer = n
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    
    def bfs(start):
        cnt = 1
        visited = [0] * (n + 1)
        visited[start] = True
        q = deque([(start)])
        
        while q:
            now = q.popleft()
            
            for i in graph[now]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
                    cnt += 1
        return cnt

    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        answer = min(abs(bfs(a) - bfs(b)), answer)
        
        graph[a].append(b)
        graph[b].append(a)
        
    return answer
    
    