# 직각삼각형

while True:
    num= list(map(int,input().split())) # 숫자를 리스트에 넣는다.
    
    if sum(num) == 0:
        break
    else:
        maxnum = max(num) # 빗변 추출 (최대값)

        num.remove(maxnum) # 빗변 리스트에서 제거

        if num[0]**2 + num[1]**2 == maxnum**2: # 피타고라스 정리 이용
            print('right')
        else:
            print('wrong')