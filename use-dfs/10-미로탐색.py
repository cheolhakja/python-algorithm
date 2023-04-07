import sys

sys.stdin = open("input.txt", "r")

dx = [-1, 0, 1, 0] #좌 하 우 상
dy = [0,1,0,-1]
cnt = 0

def DFS(x,y):
    global cnt #여기서 cnt = 10을 해버리면 지역변수 cnt를 선언하고 거기에 할당을 해버린다
    
    if tmpx == 6 and tmpy == 6:
        cnt = cnt + 1
        return
    
    else:
        for i in range(4):
            tmpx = x + dx[i]
            tmpy = y + dy[i]          
            if(0<=tmpx<=6 and 0<=tmpy<=6 and board[tmpx][tmpy] == 0):
                board[tmpx][tmpy] = 1
                DFS(tmpx, tmpy)
                board[tmpx][tmpy] = 0 #이분분은 암기 해야할듯
            else:
                continue #board의 갈 수 없는 부분을 

if __name__ == "__main__":
    board = [     list(map(int, input().split()))         for _ in range(7)]
    cnt = 0
    DFS(0,0)
    