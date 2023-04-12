import sys
from collections import deque

sys.stdin = open("input.txt", "r")
dx=[-1, -1, 0, 1, 1, 1, 0, -1]
dy=[0,1,1,1,0,-1,-1,-1]
n = int(input())


island = [ list(  map(int, input().split()))  for i in range(n)]

cnt = 0

def BFS(x,y):
    
    Q= deque()
    '''x,y를 Q에 넣는다
    pop한다
    연결되있는 노드들을 에 대하여 BFS(xx, yy)를 실행한다
    '''


Q= deque()
for i in range(n):
    for j in range(n):
        if(island[i][j] == 1):
            
            Q.append((i,j))

            while(Q):
                tmp = Q.popleft()
                for k in range(8):
                    xx = tmp[0] + dx[k]
                    yy = tmp[1] + dy[k]
                    if(0<=xx<n and 0<=yy<n and island[xx][yy] == 1):
                        Q.append((xx, yy))
                        island[xx][yy] = 0

            cnt += 1 #1이 있는 경우에만 섬의 갯수를 하나 늘려주어야되서 인덴트를 해주었음

print(cnt)
'''
어쨌든 서로 인접한 노드들을 탐색하여 섬을 구성하는 거니까.. bfs가 맞는듯!!
'''