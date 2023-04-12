import sys

sys.stdin = open("input.txt", "r")

n = int(input())
q_and_v = []

for i in range(n):
    quantity, value = map(int, input().split())
    q_and_v.append((quantity, value))

q_and_v.sort(key = lambda x:x[1], reverse = True)

def knapsack_fractional(W, w, p): #W는 가방에 담을 수 있는 최대무게, w는 배열
    K = [0] * (n+1)
    weight = 0
    for i in range(1, n+1):
        weight += w[i]
        K[i] = w[i]

if __name__ == "__main__":
