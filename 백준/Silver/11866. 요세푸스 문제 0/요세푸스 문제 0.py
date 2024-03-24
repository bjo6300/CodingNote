import sys

input = sys.stdin.readline # 시간 단축

N, K = map(int,input().split()) # N = 사람 수, K = 제거될 사람 순서
ans = []
arr = [i for i in range(1, N + 1)] 
num = 0

for i in range(N):
    num += K - 1 # K번째 사람 (인덱스로 변환)

    if num >= len(arr): # 인덱스 넘어가는 경우
        num = num % len(arr) 
    
    ans.append(str(arr[num]))
    arr.pop(num)

print("<",', '.join(ans),">", sep="")