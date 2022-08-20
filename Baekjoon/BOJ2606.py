from collections import deque

com = int(input()) # 컴퓨터의 수
connect = int(input()) # 연결된 쌍 개수
graph = [[] for _ in range(com+1)] # connect 저장 리스트 // 인덱스 0 은 사용 안함
visited = [False for _ in range(com+1)] # 방문 여부 // 인덱스 0 은 사용 안함

for _ in range(connect):
    a, b = map(int, input().split())
    # 연결된 컴퓨터의 정보가 언제가 1부터 등장한다는 보장 x
    graph[a].append(b)
    graph[b].append(a)

# bfs 구현
def bfs(x):
    deq = deque([x]) # 방문할 컴퓨터가 들어있는 deque
    count = 0 # 바이러스에 걸린 컴퓨터 수
    visited[x] = True # 방문한 컴퓨터는 True
    while deq:
        node = deq.popleft()
        for next_node in graph[node]: # 방문한 컴퓨터와 연결된 컴퓨터 체크
            if not visited[next_node]: # False일 떄 실행
                visited[next_node] = True # 방문 표시
                deq.append(next_node) # 방문 예정인 컴퓨터를 deq에 추가
                count += 1

    return count

print(bfs(1)) # 1번 컴퓨터를 통해 바이러스에 걸리게 됨.