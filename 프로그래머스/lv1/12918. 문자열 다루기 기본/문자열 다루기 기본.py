def solution(s):
    num_list = [i for i in range(1, 10)]
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True
    return False