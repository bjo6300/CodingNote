# 요세푸스 문제
import sys

input = sys.stdin.readline # 시간 단축

N, K = map(int,input().split()) # N = 사람 수, K = 제거될 사람 순서
ans= []
arr = [i for i in range(1,N+1)] 
num = 0
for i in range(N):
    num+=(K-1)
    if num >= len(arr): # num이 리스트 길이보다 크거나 같을 때 num을 나머지로 설정
        num %= len(arr)
    ans.append(str(arr[num])) # join을 쓰기 위해 str로 형변환
    arr.pop(num) # 지운것 제거

print("<",', '.join(ans),">", sep="")

# join을 써서 ' '안의 형식으로 리스트 안의 항목을 합치려면 str로 변환해야한다.
# sep=""을 하지 않으면 "< 3, 6 ... 4 >" 이런식으로 <와 3 사이에 공백이 생긴다.