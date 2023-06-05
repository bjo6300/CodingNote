n,k = map(int,input().split()) #값 입력

money=[int(input()) for _ in range(n)] 

num = 0 #코인의 총 개수 입력 변수

#큰 값이 있는 뒤의 인덱스부터 계산
for i in range(1,n+1):
    coin = money[-i]
    if k>= coin:
        coinum = k//coin #money[-i] 동전의 개수
        k -=coin*coinum #k에서 동전만큼의 가격을 뺌
        num +=coinum #총 동전의 개수 증

print(num)
