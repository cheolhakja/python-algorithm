import sys

sys.stdin = open("input.txt", "r")

n = int(input())

for i in range(n):
    s = input() #문자열을 입력받는다
    s = s.upper()
    length: int = s.__len__()
    flag: bool = True
    for j in range(length // 2):
        if(s[j] != s[-1 - j]):
            flag = False
    
    if(flag == True):print("#%d Y" %(i+1))
    else:print("#%d N" %(i+1))
