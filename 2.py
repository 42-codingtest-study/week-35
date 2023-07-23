import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n, s, e, k = list(map(int,input().split()))
    num = list(map(int,input().split()))
    res_num = num[s-1:e]
    res_num.sort()
    print("#%d %d" %(i+1, res_num[k-1]))