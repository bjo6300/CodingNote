from collections import deque

def solution(priorities, location):
    queue = deque(priorities)
    answer = 0

    while queue:
        first_priority = max(queue) # 우선순위 가장 높은 요소
        now = queue.popleft() 
        location -= 1

        if first_priority > now: # 우선순위가 아닌 경우
            queue.append(now)

            if location == -1: # 인덱스 벗어날 경우
                location = len(queue) - 1
        else: # 우선순위인 경우
            answer += 1 # 인쇄순서 +1

            if location == -1: # 내가 요청한 문서
                break  

    return answer