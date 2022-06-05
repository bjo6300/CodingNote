n = int(input())
count = 0

while n >= 0:
    # 5로 나누어 떨어질 때
    if n % 5 == 0:
        count += n // 5
        print(count)
        break
    # 5로 나누어 떨어지지 않으면 3을 빼고 count를 1 증가
    # 다시 5로 나누어 떨어지는지 확인한다.
    n -= 3
    count += 1

# 3, 5의 조합으로 안되면 -1
else:
    print(-1)