import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())

graph = [ [0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(n + 1)]
def bfs(x):
    q = deque()
    visited[x] = 1
    q.append(x)
    while q:
        a = q.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[a] + 1

bfs(1)
result = 0
for i in range(2,n+1):
    if 0 < visited[i] < 4 :
        result += 1

print(result)