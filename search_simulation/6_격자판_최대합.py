#이차원 배열 입력받는 법 복습
#input().split()의 결과가 list인데 이걸 map타입의 객체로 바꿔야한다
import sys

sys.stdin = open("input.txt", "r")
length= int(input())

square = [list(map(int, input().split())) for _ in range(length)]

result_sum_row = []
result_sum_col = []
result_sum_cross = []
for i in range(length):
    row_sum ,col_sum = 0
    for j in range(length):
        row_sum += square[i][j]
        col_sum += square[j][i]
    result_sum_row.append(row_sum)
    row_sum = 0
    result_sum_col.append(col_sum)
    col_sum = 0


cross_sum_1, cross_sum_2 = 0,0
for i in range(length):
  
    cross_sum_1 += square[i][i]
    cross_sum_2 += square[i][(length - 1) - i]

result_sum_cross.append(cross_sum_1)
result_sum_cross.append(cross_sum_2)

#미완
