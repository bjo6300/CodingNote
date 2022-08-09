# 닉네임에 갓 붙이기

for i in range(int(input())): # 닉네임 수 만큼 반복문
    nickname = input().split() # 입력 받은 닉네임을 음절단위로 분리 -> split은 리스트로 변환
    nickname[0] = 'god' # 맨 앞 음절 대신 'god' 저장
    print(''.join(nickname)) # join으로 리스트 요소를 한 줄에 출력
