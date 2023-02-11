# 대회 or 인턴

n,m,k = map(int,input().split()) # 여, 남, 인턴 참여인원

team = 0

while n >=2 and m >=1 and n+m-3>=k :
    n -=2 # 여자 2명 
    m -=1 # 남자 1명
    team +=1

print(team)