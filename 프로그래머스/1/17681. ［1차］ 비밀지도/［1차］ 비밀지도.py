def solution(n, arr1, arr2):
    secret_map = ['0' * n for _ in range(n)]
    
    for i in range(len(arr1)):
        # 2진수로 변환
        arr1_two = bin(arr1[i])[2:]
        arr2_two = bin(arr2[i])[2:]
        
        # 2진수 길이 맞추기
        if n > len(arr1_two):
            arr1_two = (n - len(arr1_two)) * "0" + arr1_two

        if n > len(arr2_two):
            arr2_two = (n - len(arr2_two)) * "0" + arr2_two
       
        # 비밀지도 해독 # or 공백
        for j in range(len(secret_map[i])):
            if arr1_two[j] == "0" and arr2_two[j] == "0":
                secret_map[i] = secret_map[i][:j] + " " + secret_map[i][j + 1:]
            else:
                secret_map[i] = secret_map[i][:j] + "#" + secret_map[i][j + 1:]
                
    return secret_map