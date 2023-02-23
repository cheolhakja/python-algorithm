import sys

sys.stdin = open("input.txt", "r")

n = int(input())

for i in range(n):
    s = input() #문자열을 입력받는다
    s = s.upper()
    s_reverse = s[::-1]
    if(s == s_reverse):
        print("YES")
    else:
        print("NO")