import sys

sys.stdin = open("input.txt", "r")

n = int(input())

bricks = []

for i in range(n):
    a, h, w = map(int, input().split())
    bricks.append((a,h,w))
    
bricks.sort(key=lambda a: a[0], reverse=True)
d = [0]*n
d[0] = bricks[0][1] #동적프로그래밍 초기화 맨위에 가장 넓은 블럭이 오려면... 그 가장 넓은 블럭 하나만 놓여야 한다


for i in range(1, len(b)):
    max_h = -2147000000
    for j in range(i-1): 
        #i가 1일때 j는 0부터 0까지/ 여기까지는 무조건 맞음
        my_weight = bricks[i][2]
        compare_weight = bricks[j][2]


        if((compare_weight > my_weight) and (max_h < d[j])): #무슨 조건이죠?: '누적 높이'가 최대인것을 찾기 (중요=누적높이라는거)
            d[i] = 
            max_h = d[]

    d[i] = max(height_of_more_weight) + b[i][1]

for i in d:
    print(i)  