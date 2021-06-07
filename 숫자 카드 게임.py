row, col = map(int, input().split())

answer = 0

for i in range(row):
    min_number = min((map(int, input().split())))
    answer = max(answer, min_number)


print(answer)