import sys
input = sys.stdin.readline

n, m = map(int, input().split())
know = set(input().split()[1:])

party_list = []
for _ in range(m):
    party_list.append(set(input().split()[1:]))

for _ in range(m):
    for party in party_list:
        if party & know:
            know = know.union(party)

cnt = 0
for party in party_list:
    if not party & know :
        cnt += 1

print(cnt)