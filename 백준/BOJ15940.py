import sys

input1 = sys.stdin.readline()

UCPC = ['U','C','P','C']

# True면 I love UCPC, False면 I hate UCPC
flag = True

for i in range(len(UCPC)):
    if UCPC[i] in input1:
        flag = True
        
        # find(문자) => 문자의 인덱스 반환
        index = input1.find(UCPC[i])
        
        # 인덱스로 슬라이싱해서 i 문자 제거
        input1 = input1[index+1:]
    else:
        flag = False

        # break를 안걸면 존재하지 않았을때도 다시 for문이 돌아가서 flag가 True로 된다.
        break

if flag == True:
    print('I love UCPC')
else :
  print('I hate UCPC')