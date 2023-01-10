def solution(n):
    lst = list(str(n)) # n을 문자로 형변환 후 list 생성
    lst.sort(reverse = True) # 내림차순으로 정렬
    return int(''.join(lst)) # 정렬된 문자를 합친 후 int로 형변환