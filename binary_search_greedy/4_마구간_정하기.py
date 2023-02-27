import sys

sys.stdin = open("input.txt", "r")

line = []
res = 0
n, c = 0,0

n,c = map(int, input().split())
for i in range(n):
    tmp = int(input())
    line.append(tmp)

def count(mid: int) -> int :
    num = 1

    previous_index = line[0]
    for i in range(1, len(line)):
        if((line[i] - previous_index) >= mid):
            num += 1
            previous_index = line[i]
            
    '''
    최소기준 이상의 간격을 충족시키면서 말을 몇개나 배치할 수 있나 세는 코드
    '''
    return num

line.sort()
lp = line[0]
rp = line[n - 1]
while lp <= rp :
    mid = (lp + rp)//2
    
    if count(mid) >= c:
        res = mid
        lp = mid + 1
    else:
        rp = mid - 1

print(res)

# 답을 정하고 이 답이 유효한지 확인해 가면서 더 좋은 답을 찾아가는 방식입니다. 답을 찾는 과정은 주로 이분검색을 사용하구요.
# 이분탐색 알고리즘 문제였음
# 복습 요함. 뭔지 잘 모르겠음.