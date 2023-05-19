t = int(input())

for i in range(1, t + 1):
    testcase = map(int, input().split())
    print("#" + str(i), round(sum(testcase) / 10))