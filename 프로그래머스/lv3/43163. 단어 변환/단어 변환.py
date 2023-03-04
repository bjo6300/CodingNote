from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0]) # 알파벳, 단계 
    visited = [ 0 for i in range(len(words))] 
    
    while q:
        word, cnt = q.popleft() # 알파벳, 단계 
        if word == target: # 답과 같으면 break
            answer = cnt
            break        
        for i in range(len(words)): # 단어의 집합만큼 반복
            temp_cnt = 0 # 한번에 한 개의 알파벳만 바꿀 수 있어서 체크하는 용도
            if not visited[i]:
                for j in range(len(word)): # 단어의 길이만큼 반복
                    if word[j] != words[i][j]: # 알파벳이 다르면 +1
                        temp_cnt += 1
                if temp_cnt == 1: # 알파벳이 1개만 다를 때 q에 저장
                    q.append([words[i], cnt+1])
                    visited[i] = 1
                    
    return answer