def solution(wallpaper):
    answer = []
    row = []
    col = []
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                row.append(i)
                col.append(j)
    
    answer.append(min(row))
    answer.append(min(col))
    answer.append(max(row) + 1)
    answer.append(max(col) + 1)
    
    return answer