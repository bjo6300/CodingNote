# 쉽게 푸는 문제

A,B = map(int,input().split()) # A=시작, B=끝

count = 0 # A의 값
result = 0 # A의 값을 다 더한 최종 결과
i = 1 # A에서 뺄 것

while A != B+1: # 1 ≤ A ≤ B ≤ 1,000
    count += i
    if A - count > 0:
        i += 1
    else:
        result += i # A의 최종결과 저장
        A+=1 # A를 1 증가해서 다시 A에 해당하는 숫자 찾기
        i = 1 # i 초기화 
        count = 0 # count 초기화

print(result)

# 3 >= 1 + 2   -> 2
# 7 >= 1 + 2 + 3 //  7 < 1 + 2 + 3 + 4     -> 4