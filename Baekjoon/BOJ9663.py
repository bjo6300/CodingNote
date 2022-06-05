# N-Queen

N = int(input())

ans = 0
row = [0] * N # 열

def is_promising(x):
    # row[x] == row[i] -> 열 체크
    # abs(row[x] - row[i]) == abs(x - i) -> 대각선 체크
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == N: # N개의 퀸을 다 놓은 경우
        ans += 1 
        return

    else:
        for i in range(N):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(ans)