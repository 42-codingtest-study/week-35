# code.plus - 이전 순열

n = int(input())
data = list(map(int, input().split()))

for i in range(n - 1, 0, -1) :
    if data[i] < data[i - 1] :
        x, y = i - 1, i
        for j in range(n - 1, 0, -1) :
            if data[j] < data[x] :
                data[j], data[x] = data[x], data[j]
                data = data[:i] + sorted(data[i:], reverse = True)
                print(*data)
                exit(0)
print(-1)