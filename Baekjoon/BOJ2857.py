# FBI
data = [] # FBI 첩보원명

for _ in range(5) :
  data.append(input())

flag = 0

for i in range(len(data)) :

  if 'FBI' in data[i] :
    print(i+1, end=' ') # 인덱스가 0부터 시작해서 i+1
    flag = 1

if flag == 0 :
  print('HE GOT AWAY!')