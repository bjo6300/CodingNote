# 수 뒤집기
T = int(input())

for _ in range(T):
    N = input()
    
    sum_n = str(int(N) + int(N[::-1])) # 수를 뒤집기 위한 str로 형변환

    if sum_n == sum_n[::-1]:
        print("YES")
    else:
        print("NO")