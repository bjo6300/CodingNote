def solution(X, Y):
    result = ''
    a = [0,0,0,0,0,0,0,0,0,0]
    b = [0,0,0,0,0,0,0,0,0,0]
    
    for i in X: # X에 0~9까지 숫자가 몇개 있는지 count
        value = int(i)
        a[value] += 1
    
    for i in Y: # Y에 0~9까지 숫자가 몇개 있는지 count
        value = int(i)
        b[value] += 1
    
    for i in range(9, -1, -1): # 9~0까지 count한 수 중에서 최소값을 result에 추가
        result += str(i) * min(a[i],b[i]) 
 
    if(len(result) == 0): # ''이면 '-1' 반환
        return '-1'
    if(result[0] == '0'): # 000이더라도 '0' 반환
        return '0'
              
    return result