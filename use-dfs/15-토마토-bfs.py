import sys
from collections import deque

sys.stdin = open("input.txt", "r")
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == "__main__":
    m,n = map(int, input().split())  #n이 행, m이 열
    t = [   list(  map(int, input().split())) for _ in range(n)] #t는 토마토의 약자
    dis = [m * [0]  for _ in range(m)]
    Q = deque()
    '''for i in range(n):
        for j in range(m):
            if t[i][j] == 0:
                unrotten_num += 1 #토마토가 안익은 영역의 갯수k를 샌다
'''
    for i in range(n):
        for j in range(m):
            if t[i][j] == 1:
                Q.append((i,j)) #행과 열 순서로 저장한다
                
    while Q:
        tmp = Q.popleft()
        for i in range(4):           
            x = tmp[0] + dx[i]
            y = tmp[1] + dy[i]
            t[x][y] = 1
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1
            Q.append((x,y))
                #if 인접한 토마토가 존재하고, 토마토가 사각형 범위안에 있고, 아직 안익었으면
                #   그 토마토를 익게하고
                #   그 토마토를 queue에 넣고
                #   queue_num을 +=1
                #   전체 안익은 토마토의 갯수를 +=1 해준다

    max_num = -2147000
    for i in range(n):
        for j in range(m):
            if t[i][j] > max_num:
                max_num = t[i][j]
    print(max_num)
       
    