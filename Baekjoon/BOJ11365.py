# !밀비 급일

while True:
    password = input()
    if password == "END":
        break
    else:
        password = password[::-1]
        print(password)
