import sys

sys.stdin = open("input.txt", "r")

n = int(input())

for i in range(n):
    s = input() #문자열을 입력받는다
    s = s.upper()
    length: int = s.__len__()
    flag: bool = True
    for i in range(length // 2):
        if(s[i] != s[length -1 - i]):
            flag = False
    
    if(flag == True):print("Y")
    else:print("N")
