N, M = map(int, input().split())

result = 0

while True:
    # (N == K 로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (N // M) * M
    result += (N - target)
    N = target

    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if N < M:
        break

    result += 1
    N //= M



result += (N - 1)
print(result)