# 2022 SK텔레콤 T-WorX for Developers 챌린지

# 3번

def solution(n, plans, clients):
    # 부가서비스 수, 요금제 정보(제공데이터, 추가 부가서비스), 이용하려는 서비스 정보(제공데이터, 추가 부가서비스)
    answer = [0 for _ in range(len(clients))]

    plans_split = []
    for i in range(len(plans)):
        a = plans[i].split()
        plans_split.append(a)

    clients_split = []
    for i in range(len(clients)):
        a = clients[i].split()
        clients_split.append(a)

    for i in range(len(plans_split)-1): 
        plans_split[i+1] += plans_split[i][1:]
        
    temp = 0
    money = 0
    
    # 부가서비스 먼저 비교 후 요금제 최소 찾기 
    for i in range(len(plans)-1):
        for j in range(len(clients_split[1:])-1):
            if clients_split[i][j+1] in plans_split[i][1:]:
                temp = 1
                continue
            else:
                temp = 0
                break
        if temp == 1:
            money = plans_split[i][0]
            print(money)    


    print(plans_split)
    print(clients_split)



   
    return print(answer)

solution(5, ["100 1 3", "500 4", "2000 5"], ["300 3 5", "1500 1", "100 1 3", "50 1 2"])



# # 2번

# def solution(periods, payments, estimates):
#     #기간, 여태 낸 금액, 앞으로 납부할 금액 
#     answer = [0,0]
#     answer_process = [[0,0] for _ in range(len(periods))]
    
#     for i in range(len(periods)):
#         # 이번달
#         # 가입기간 2년이상
#         if periods[i] >= 24 and periods[i]<60:
#             # 90만원 이상
#             if sum(payments[i]) >= 900000:
#                 answer_process[i][0] += 1 # vip
#         elif periods[i] >= 60:
#             if sum(payments[i])>= 600000:
#                 answer_process[i][0] +=1

#         # 다음달
#         # 2년 이상 5년 미만
#         if periods[i]+1 >= 24 and periods[i]+1<60:
#             if sum(payments[i][1:]) + estimates[i]>= 900000:
#                 answer_process[i][1] +=1
#         # 5년 이상
#         elif periods[i]+1 >=60:
#             if sum(payments[i][1:]) + estimates[i]>= 600000:
#                 answer_process[i][1] +=1

#     for j in range(len(periods)):
#         if answer_process[j][0] == 0 and answer_process[j][1] >= 1:
#             answer[0] += 1
#         elif answer_process[j][0] >= 1 and answer_process[j][1] == 0:
#             answer[1] += 1
    
#     return answer
#     # return print(answer)

# # 1번
# def solution(p):
#     answer = [0 for _ in range(len(p))]
    
#     for i in range(len(p)):
        
#         min_idx = p.index(min(p))

#         if p[i] != min(p):
#             answer[min_idx] += 1
#             answer[i] += 1
#             p[i],p[min_idx] = p[min_idx], p[i]
#             p[i] = max(p)
#         else :
#             p[i] = max(p)
#             continue
       
#     return answer