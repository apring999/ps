def recur(cnt, total, plus, minus, mul, div):
    global min_result
    global max_result

    if cnt == N:
        # 최대, 최소 계산
        min_result = min(min_result, total)
        max_result = max(max_result, total)
        return

    # 덧셈
    if plus > 0:
        recur(cnt + 1, total + numbers[cnt], plus - 1, minus, mul, div)
    # 뺄셈
    if minus > 0:
        recur(cnt + 1, total - numbers[cnt], plus, minus - 1, mul, div)
    # 곱셈
    if mul > 0:
        recur(cnt + 1, total * numbers[cnt], plus, minus, mul - 1, div)
    # 나눗셈
    if div > 0:
        recur(cnt + 1, int(total / numbers[cnt]), plus, minus, mul, div - 1)

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    opers = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    min_result = 1e9
    max_result = -1e9

    recur(1, numbers[0], opers[0], opers[1], opers[2], opers[3])
    print(f'#{tc} {max_result - min_result}')