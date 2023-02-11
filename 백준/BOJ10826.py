# 피보나치 수 4

n = int(input())

x, y = 0, 1 # x는 현재값, y는 다음값

# 현재값과 이전값을 더해 다음 값을 구한다.
for _ in range(n):
    x, y = y, x+y

print(x)