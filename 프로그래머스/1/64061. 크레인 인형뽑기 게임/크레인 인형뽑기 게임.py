def solution(board, moves):
    answer = 0
    bucket = []
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] != 0: # 0이 아닐 경우
                temp = board[j][i - 1] # 바구니에 넣을 요소
                board[j][i - 1] = 0
                
                if len(bucket) != 0: # 바구니 길이가 0이 아닌 경우
                    top = bucket.pop()
                    
                    if top == temp:
                        answer += 2
                    else:
                        bucket.append(top)
                        bucket.append(temp)
                else: # 바구니 길이가 0인 경우
                    bucket.append(temp)
                    
                break
                    
    return answer