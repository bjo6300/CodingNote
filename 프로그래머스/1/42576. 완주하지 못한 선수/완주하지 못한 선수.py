def solution(participant, completion):
    answer = ''

    # 두 리스트 정렬
    participant.sort()
    completion.sort()

    # 없는 사람 찾기
    for i in range(len(completion)):
        if(participant[i] != completion[i]):
            return participant[i]

    # 전부 다 돌아도 없을 경우에는 마지막 주자가 완주하지 못한 선수
    return participant[len(participant)-1]