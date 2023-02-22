def solution(routes):
    # 0 : i번째 차량이 고속도로에 진입한 지점
    # 1 : i번째 차량이 고속도로에서 나간 지점
    routes.sort(key = lambda x: x[1]) # 나간지점을 기준으로 정렬
    answer = 1
    now_out = routes[0][1]
    # print(routes)
    
    for i in range(1, len(routes)):
        if now_out < routes[i][0]:
            now_out = routes[i][1]
            answer += 1
            
    return answer 
