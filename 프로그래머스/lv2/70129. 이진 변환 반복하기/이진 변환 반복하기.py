def solution(s):
    zero_cnt = 0
    binary_cnt = 0
    def count_zero(num):
        return num.count('0')

    def remove_zero(num):
        num = num.replace('0', "")
        return num

    def binary(num):
        b = bin(num)
        return b[2:]
    
    while True:
        if s == "1":
            break
        zero_cnt += count_zero(s)
        s = remove_zero(s)
        s = binary(len(s))
        binary_cnt += 1
        
    return [binary_cnt, zero_cnt]

print(solution("110010101001"))