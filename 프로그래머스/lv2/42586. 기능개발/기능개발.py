from collections import deque
def solution(progresses, speeds):
    answer = []
    deploy = deque()
    
    for i in range(len(progresses)):
        day = 0
        
        while True:
            day += 1
            progresses[i] += speeds[i]
            
            if progresses[i] >= 100:
                deploy.append(day)
                break
                
    print(list(deploy))
    
    dep = deploy.popleft() # 배포 날짜

    when_dep = 1
    
    for function in list(deploy):
        if dep >= function:
            deploy.popleft()
            when_dep += 1
        else:
            answer.append(when_dep)
            dep = deploy.popleft()
            when_dep = 1

    answer.append(when_dep)
    
    return answer