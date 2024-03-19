from collections import deque
def solution(bridge_length, weight, truck_weights):
    
    time = 0
    bridge = deque([0] * bridge_length) # 다리 길이만큼 0으로 채운다.
    truck_weights = deque(truck_weights)
    current_weight = 0
    
    while len(truck_weights) != 0:
        time += 1

        current_weight -= bridge.popleft()

        if current_weight + truck_weights[0] <= weight: # 다리가 새로운 트럭을 견딜 수 있다면
            truck = truck_weights.popleft() 

            # 트럭 추가
            current_weight += truck 
            bridge.append(truck)
        else: # 아니면 0을 추가해 다리 길이 유지
            bridge.append(0)
            
    time += bridge_length # 마지막 트럭 시간 추가
    
    return time