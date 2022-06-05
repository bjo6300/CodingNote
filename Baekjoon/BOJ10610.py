# 30

# 시간초과 max, remove가 각각 O(N)이라 시간복잡도가 높음
N = list(input())
N = list(map(int, N))
N.sort(reverse=True)

if (sum(N) % 3 == 0) & (0 in N):
    N=list(map(str,N))
    print(''.join(N))
else:
    print('-1')

# # 다른사람 코드
# n = list(input())
# n.sort(reverse=True) # O(N log N)
# sum = 0
# for i in n: # O(N)
#     sum += int(i)
# if sum % 3 != 0 or "0" not in n: # 3으로 나누어 떨어지고 0이 있어야 30으로 나누어 떨어짐
#     print(-1)
# else:
#     print(''.join(n))