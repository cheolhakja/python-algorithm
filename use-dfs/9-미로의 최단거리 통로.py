# 이 문제 어려움. 미로에서 최단거리 BFS라는거 외워야될듯

import sys
from collections import deque

sys.stdin = open("input.txt", "r")

dx = [-1, 0, 1, 0] #좌 하 우 상
dy = [0,1,0,-1]
board = [     list(map(int, input().split()))         for _ in range(7)]
dis = [     [0] * 7      for _ in range(7)]
Q = deque()
Q.append((0,0))
board[0][0] = 1

while Q:
    tmp = Q.popleft()
    for i in range(4):
        xx = tmp[0] + dx[i]
        yy = tmp[1] + dy[i]     
        if(0<=xx<=6 and 0<=yy<=6 and board[xx][yy] == 0):
            board[xx][yy] = 1
            dis[xx][yy] = dis[tmp[0]][tmp[1]] + 1
            Q.append((xx,yy))

if(dis[6][6] == 0):
    print(-1)
else:
    print(dis[6][6])

    