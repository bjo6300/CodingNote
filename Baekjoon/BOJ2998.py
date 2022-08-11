# 8진수

two_to_eight = {
    '000': '0',
    '001': '1',
    '010': '2',
    '011': '3',
    '100': '4',
    '101': '5',
    '110': '6',
    '111': '7'
}

num = input()
result = ""

while len(num) % 3 != 0: # 길이가 3의 배수일떄까지 앞에 0 추가
    num = "0" + num

while num:
    result = result + two_to_eight[num[0:3]] # 키에 맞는 값을 result에 추가
    num = num[3:] # 추가한 num을 제거

print(result)