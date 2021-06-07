N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

arr.sort(reverse=True)

first = arr[0]
second = arr[1]

# for i in range(M):
#     if i != 0 and K % i == 0:
#         answer += second
#     else:
#         answer += first

#가장 큰 수가 더해지는 횟수 계산
count = int(M / (K + 1)) * K
count += M % (K + 1)

answer += count * first
answer += (M - count) * second

print(answer)