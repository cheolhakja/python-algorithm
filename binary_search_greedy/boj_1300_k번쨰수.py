import sys

sys.stdin = open("input.txt", "r")

n = int(input())
k= int(input())

A = []
for i in range(1, n+1):
    subset = []
    for j in range(1, n + 1):
        subset.append(i * j)
    A.append(subset)

result = []
for i in A:
    for j in i:
        result.append(j)

result.sort()
print(result[k])

# 범위를 줄여가면서 수를 추측하기. 정사각형과 제곱수의 특성을 고려해야됨. 1 -> 4 -> 9..