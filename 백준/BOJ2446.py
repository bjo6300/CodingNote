# 별 찍기 - 9

n = int(input())

space = 0

for i in range(n, 0, -1):
    print(space*' '+ '*'*(2*i-1))
    space+=1

space-=2

for j in range(2,n+1):
    print(space*' '+ '*'*(2*j-1))
    space-=1