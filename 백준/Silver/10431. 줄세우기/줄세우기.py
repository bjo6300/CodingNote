import sys
input = sys.stdin.readline
from collections import deque

n = int(input().rstrip())

for i in range(n):
    walk = 0
    students = deque(list(map(int, input().rstrip().split())))
    students.popleft()
    line = []
    
    line.append(students[0])
        
    for j in range(1, len(students)):
        if students[j] > line[-1]:
            line.append(students[j])
            continue

        for k in range(len(line)):
            if students[j] < line[k]:
                new_line = line[:k] + [students[j]] + line[k:]
                walk += len(line[k:])
                line = new_line
                break
                
    print(str(i + 1) + " " + str(walk))
