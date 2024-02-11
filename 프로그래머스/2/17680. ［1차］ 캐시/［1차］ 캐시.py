from collections import deque

def solution(cacheSize, cities):
    total_time = 0
    q = deque()
    
    if cacheSize == 0: # 캐시사이즈 0인 경우
        return len(cities) * 5
    
    for i in cities:
        i = i.upper()
        
        if i in q: # q에 있는 경우
            q.remove(i)
            q.appendleft(i)
            total_time += 1
            
        elif i not in q: # q에 없는 경우
            q.appendleft(i)
            total_time += 5
                
            if cacheSize < len(q):
                q.pop()
            
    return total_time