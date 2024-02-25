def solution(dartResult):
    idx = -1
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    nums = [0, 0, 0]
    dartResult = dartResult.replace("10", "t")
    
    for i in dartResult:
        # 숫자
        if i in num:
            idx += 1
            nums[idx] = int(i)
        # t = 숫자 10인 경우
        elif i == 't':
            idx += 1
            nums[idx] = 10
        # SDT (S는 숫자 그대로)
        elif i == 'D':
            nums[idx] *= nums[idx]
        elif i == 'T':
            nums[idx] *= nums[idx] * nums[idx]
        # 옵션(*, #)
        elif i == '*':
            if idx == 0: # 인덱스 0인 경우
                nums[idx] *= 2
            else:
                nums[idx - 1] *= 2
                nums[idx] *= 2
        elif i == '#':
            nums[idx] *= -1
            
    return sum(nums)