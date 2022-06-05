# 균형잡힌 세상
while True:
    x=input().rstrip()

    if x=='.': # .이면 종료
        break

    stack=[]
    result=True

    for i in x:
        if i=='[' or i=='(': # 괄호 저장
            stack.append(i)
        elif i==']': 
            if not stack: # 스택에 아무것도 없을 때
                result=False
                break
            if stack[-1]=='[': # 마지막이 [ 일때 pop
                stack.pop()
            else:
                result==False
                break
        elif i==')': 
            if not stack: # 스택에 아무것도 없을 때
                result=False
                break
            if stack[-1]=='(': # 마지막이 ( 일때 pop
                stack.pop()
            else:
                result==False
                break

    if result and not stack: # result가 True고 스택이 비어있을 때
        print('yes')
    else:
        print('no')