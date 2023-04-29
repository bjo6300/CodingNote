import sys
input = sys.stdin.readline

m, n  = map(int,input().split())
snacks = list(map(int, input().split()))
start = 1 # 과자의 길이는 1 이상
end = max(snacks)
answer = 0

while start <= end:
    mid = (start + end) // 2
    c = 0 # 길이가 mid인 것을 만들 수 있는 개수
    
    for snack in snacks:
        c += snack // mid

    if c >= m:
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1

print(answer)