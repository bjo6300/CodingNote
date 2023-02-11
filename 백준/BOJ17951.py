# 흩날리는 시험지 속에서 내 평점이 느껴진거야
n,k = map(int, input().split())
array = list(map(int, input().split()))

left = 0
right = sum(array) + 1
answer = 0

while left <=right:
    mid = (left+right)//2
    count = 0
    score = 0
    for i in array:
        score += i
        if score >= mid:
            count += 1
            score = 0
    if count < k:
        right = mid-1
    else:
        answer = mid
        left = mid+1

print(answer)