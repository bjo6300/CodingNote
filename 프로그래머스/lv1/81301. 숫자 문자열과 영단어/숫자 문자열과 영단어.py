def solution(s):
    nums = "0123456789"
    num_english = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    answer = ""
    temp = ""
    for i in range(len(s)):
        if s[i] in nums:
            answer += s[i]
        else:
            temp += s[i]
            for j in range(len(num_english)):
                if num_english[j] == temp:
                    answer += nums[j]
                    temp = ""
    
    return int(answer)