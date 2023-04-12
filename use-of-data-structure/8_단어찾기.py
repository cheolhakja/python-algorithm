import sys

sys.stdin = open("input.txt", "r")

n = int(input())

a = dict()

for i in range(n):
    tmp = input()
    a[tmp] = 1

for j in range(n-1):
    tmp = input()
    a[tmp] = 0

for key, value in a.items():
    if(value == 1):
        print(key)
        break

 

# 노트에 적힌 n개의 글자를 dict에 저장한다(이때 value는 1이다)
# (그다음에) 시에 적힌 n-1개의 글자를 dict에 저장한다(이때 value는 0이다)
# value가 1인 단어들이 value가 0인 단어들로 덮어씌워진다
'''
해쉬는 키-값의 자료구조로 dict가 해쉬테이블과 같은 구조이다
'''
