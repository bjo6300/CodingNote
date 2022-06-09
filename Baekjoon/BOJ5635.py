# 생일

n = int(input())
student = [] # 학생정보를 담을 리스트

for _ in range(n):
    name, dd, mm, yyyy = input().split() # 이름, 일, 월, 연도 저장
    student.append([name, int(dd), int(mm), int(yyyy)]) # 리스트로 묶어서 학생정보를 student 리스트에 저장

student.sort(key=lambda x:(x[3], x[2], x[1])) # x[3] : 연도, x[2] : 월, x[1] : 일 로 정렬
print(student[-1][0]) # 나이가 가장 적은 사람 이름
print(student[0][0]) # 나이가 가장 많은 사람 이름

# student를 출력하면 
# [['Jerry', 18, 9, 1990], ['Garfield', 20, 9, 1990], ['Alice', 30, 12, 1990], ['Mickey', 1, 10, 1991], ['Tom', 15, 8, 1993]]
# 이렇게 나오므로 인덱스를 지정해서 원하는 값을 뽑아낸다.
