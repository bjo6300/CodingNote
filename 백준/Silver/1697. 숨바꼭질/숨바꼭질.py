import sys
input = sys.stdin.readline
from collections import deque

def bfs(n):
    q = deque()             # deque는 양쪽에서 입출력 가능
    q.append(n)             # q = deque([5])
    while q:
        now = q.popleft()     # 처음 시작점은 x = 5, q = deque([])
        
        if now == k:
            print(dist[now])
            break
        
        for nx in (now - 1, now + 1, now * 2):    # nx = 4, 6, 10인 3가지 경우로 각각 for문 돌아간다.
            if 0 <= nx <= 100000 and not dist[nx]:
                dist[nx] = dist[now] + 1
                q.append(nx)    # q = deque([4, 6, "10"])

dist = [0] * (100000 + 1)      # 이동하는 거리를 알기 위한 변수
n, k = map(int, input().rstrip().split())

bfs(n)