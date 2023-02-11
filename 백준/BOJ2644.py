# 촌수계산

# 전체 사람수 => 정점 개수
# 촌수를 계산해야하는 두 사람의 번호 
# 부모자식들간의 관계개수  => 간선 개수
# 부모 자식간의 관계를 나타내는 번호 x,y => 그래프 값들

import sys
from collections import deque

input = sys.stdin.readline # 시간 단축

n = int(input()) # 전체 사람수 => 정점 개수
p1,p2 = map(int,input().split()) # 촌수를 계산해야하는 두 사람의 번호 
m = int(input()) # 부모자식들간의 관계개수  => 간선 개수

visited = [False] * (n+1)
graph=[[] for _ in range(n+1)] # 간선의 개수 + 1 만큼 생성

for _ in range(m): # 부모 자식간의 관계를 나타내는 번호 x,y => 그래프 값들
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(p1):
    queue = deque()
    queue.append(p1)
    visited[p1] = True
    result = 0
    while queue:
        result += 1
        for _ in range(len(queue)):
            n = queue.popleft()
            if n == p2:
                return result-1
            for i in graph[n]:
                if visited[i] == False:
                    visited[i] = True
                    queue.append(i)

    return -1

print(bfs(p1))