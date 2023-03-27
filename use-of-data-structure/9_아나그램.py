import sys

sys.stdin = open("input.txt", "r")

str1 = input()
str2 = input()

a = dict()
b = dict()

for i in str1: #문자열에서 char하나씩을 탐색한다
    tmp = a.get(i, 0) #char이 dict에 저장되있으면 그 갯수를 출력하고 아니면 0을 출력한다
    a[i] = tmp + 1 #해당 char의 갯수를 업데이트(+1) 한다

for i in str2: 
    tmp = b.get(i, 0) 
    b[i] = tmp + 1 

for i in a.keys(): #str1과 str2를 비교하기 위해 str1의 키들을 콜렉션으로 불러온다
    if i in b.keys():
        #str1에 있는 키가 str2에도 있으면
        if(a[i] == b[i]):
            continue #char의 갯수가 같은지 체크하는 if문
        else:
            print("no")
            break
    else:
        print("no")
        break
else:
    print("yes")
# 문제의 전제: 길이가 같은 두 문자열임,,