from itertools import combinations
 
L, C = map(int,input().split())
alpha = sorted(input().split()) # 알파벳 순으로 정렬
words = combinations(alpha, L)
 
for word in words:
    cnt_vow = 0

    for i in word: # 모음 있는지 검사
        if i in "aeiou":
            cnt_vow += 1
 
    if cnt_vow >=1 and L - cnt_vow >=2: # 전체 길이 - 모음 개수가 2 이상이면 자음의 개수가 2개 이상
        print(''.join(word))