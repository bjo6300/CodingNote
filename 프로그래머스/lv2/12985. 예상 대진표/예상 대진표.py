def solution(n,a,b):
    cnt = 0
    while True:
        if a == b:
            break
        
        if a % 2 == 0:
            a = a // 2
        elif a % 2 == 1:
            a = a // 2 + 1
        
        if b % 2 == 0:
            b = b // 2
        elif b % 2 == 1:
            b = b // 2 + 1
        
        if a > b:
            a, b = b, a
        
        cnt += 1

    return cnt