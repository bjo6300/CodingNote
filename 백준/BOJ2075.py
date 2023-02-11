# N번째 큰 수
import heapq
import sys

N = int(input())

heap = [] # min heap 첫번째 요소만 최소, 나머지는 정렬안됨
#heap에 N개의 요소를 넣어두고 heap[0]으로 N번째 큰 수를 구한다.

for _ in range(N):
    nums = list(map(int,sys.stdin.readline().split()))

    if not heap: # heap이 비어있으면 nums 추가
        for num in nums:
            heapq.heappush(heap,num) 
    else: # 비어있지 않으면 heap[0]보다 큰 값을 heap에 추가
        for num in nums:
            if heap[0] < num:
                heapq.heappush(heap,num)
                heapq.heappop(heap)
    
print(heap[0])