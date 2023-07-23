N = int(input())
answer, _sum = 0, 0
i = 1
while _sum <= N:
    _sum += i
    if (N - _sum) >= 0 and (N - _sum) % i == 0:
        answer += 1
    i += 1
print(answer)
