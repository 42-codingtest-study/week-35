# code.plus - 로또

# 라이브러리 사용 (재귀 x)
import itertools

while True :
    array = list(map(int, input().split()))
    k = array[0]
    s = array[1:]
    for i in itertools.combinations(s, 6) :
        print(*i)

    if k == 0 :
        exit()
    print()