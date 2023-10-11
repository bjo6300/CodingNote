def solution(n, arr1, arr2):
    # 이진수 변환 함수 : format(i, 'b')
    total_map = [[0]*n for _ in range(n)] # nxn 지도
    map1 = [[0]*n for _ in range(n)] # map1
    map2 = [[0]*n for _ in range(n)] # map2
    
    # map1 변환
    for i in range(len(arr1)):
        bin_1 = format(arr1[i], "b") # ex. 9 -> 1001
        if len(bin_1) < n:
            diff = n - len(bin_1) # if n=5인데 bin_1 = 1001이면 01001로 만들어주기 위함
            bin_1 = diff*"0" + bin_1

        for j in range(len(bin_1)):
            map1[i][j] = bin_1[j]
            
    # map2 변환
    for i in range(len(arr2)):
        bin_2 = format(arr2[i], "b") # ex. 9 -> 1001
        if len(bin_2) < n:
            diff = n - len(bin_2) # if n=5인데 bin_1 = 1001이면 01001로 만들어주기 위함
            bin_2 = diff*"0" + bin_2
        for j in range(len(bin_2)):
            map2[i][j] = bin_2[j]
            
    # 전체 지도 병합
    # 규칙 : 하나라도 0(공백)이면 전체도 0, 둘다 1(벽)이어야만 전체도 1
    for i in range(n):
        map1_i = map1[i] # list의 i번째 list
        map2_i = map2[i] # list의 i번째 list
        
        for j in range(n):
            a = map1_i[j] # map1[i][j]
            b = map2_i[j] # map2[i][j]
            
            # 규칙 1
            if a == "1" or b == "1":
                total_map[i][j] = "#"
            elif a == "0" and b == "0":
                total_map[i][j] = " "
    
    answer = []
    for i in range(n):
        map_i = total_map[i]
        sum_i = map_i[0]
        for j in range(1, len(map_i)):
            sum_i = sum_i + map_i[j]
        answer.append(sum_i)
    
    return answer