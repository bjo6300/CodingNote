# 게임

import sys
input = sys.stdin.readline

X , Y = map(int,input().rstrip().split()) # 게임 횟수, 이긴게임

Z = Y * 100 // X # 승률 : 소수점 버린다.

start = 1
end = 1000000000
ans = 0

if Z >= 99: # Z가 변하지 않는 경우
    print(-1)
else:

    while start<=end:

        mid = (start+end)//2

        if (Y+mid)*100 // (X+mid) > Z:
            # 이긴게임+mid의 승률 > 현재 승률
            ans = mid
            end = mid - 1

        else: # 이긴게임 + mid 승률 < 현재 승률
            start = mid+1 # mid를 더해 승률을 높인다.

    print(ans)