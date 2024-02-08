def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        arr = []
        for j in range(len(arr2[0])):
            result = 0
            
            for k in range(len(arr1[0])):
                result += arr1[i][k] * arr2[k][j]
                
            arr.append(result)
            
        answer.append(arr)
    return answer