import math

def solution(n, k):
    answer = []
    num_list = [i for i in range(1, n+1)] # 사람들
    while (n != 0):
        temp = math.factorial(n) // n # 맨 앞자리를 제외한 나머지 자리들의 경우의 수
        index = k // temp # temp가 몇 번 지나갔는지
        k = k % temp # temp가 지나가고 나머지

        if k == 0: # 나누어 떨어져서 index - 1을 answer에 추가
            answer.append(num_list.pop(index-1))
        else: 
             answer.append(num_list.pop(index))

        n -= 1
    
    return answer

print(solution(3, 5))