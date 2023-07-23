import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    isCycle = False
    q = deque()
    q.append(start)
    
    while q:
        cnt_node = q.popleft()
        if visited[cnt_node]:
            isCycle = True
        visited[cnt_node] = 1
        for adj_node in graph[cnt_node]:
            if visited[adj_node] == 0:
                q.append(adj_node)
                
    return isCycle

case = 1
while (True) :
	n, m = map(int, input().split())
	if n != 0 or m != 0 :
		graph = [[] for _ in range(n+1)]
		visited = [0]*(n+1)
		cnt = 0
		for _ in range(m):
			a, b = map(int, input().split())
			graph[a].append(b)
			graph[b].append(a)
		for node in range(1, n+1):
			if visited[node] == 0:
				if not bfs(node):
					cnt += 1
		if cnt == 1:
			print(f'Case {case}: There is one tree.')
		elif cnt == 0:
			print(f'Case {case}: No trees.')
		else:
			print(f'Case {case}: A forest of {cnt} trees.')
		case += 1
	else :
		break