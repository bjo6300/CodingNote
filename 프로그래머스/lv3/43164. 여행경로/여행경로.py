def solution(tickets):
    # 1. 그래프 생성
    routes = dict()

    for (start, end) in tickets:
        routes[start] = routes.get(start, []) + [end]  

    # 2. 시작점 - [끝점] 역순으로 정렬    
    for r in routes.keys():
        routes[r].sort(reverse=True)

    # 3. DFS 알고리즘으로 path를 만들어줌.
    st = ["ICN"]
    path = []
    
    while st:
        top = st[-1] # 마지막에 추가된 요소

        if top not in routes or len(routes[top]) == 0: # top이 routes에 없거나 routes[top]의 길이가 0일 때
            path.append(st.pop()) # path에 저장
        else:
            st.append(routes[top][-1]) # routes의 마지막 원소 st에 추가
            routes[top] = routes[top][:-1] # routes의 마지막 원소까지 슬라이싱
    
    # 4. 만든 path를 거꾸로 돌림. 역순으로 저장되어 있기 때문
    answer = path[::-1]
    return answer

solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])