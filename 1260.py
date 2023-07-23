import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
#2차원배열 생성
matrix = [[0] * (N + 1) for i in range(N + 1)]

for i in range(M):
	a, b = map(int, input().split())
	matrix[a][b] = 1
	matrix[b][a] = 1

visited = [0] * (N + 1)

def bfs(V):
	queue = [V]
	visited[V] = 0

	while queue:
		V = queue.pop(0)
		print(V, end=' ')
		for i in range(1, N+1):
			if (matrix[V][i] == 1 and visited[i] == 1):
				queue.append(i)
				visited[i] = 0
def dfs(V):
	visited[V] = 1

	print(V, end=' ')
	for i in range(1, N+1):
		if (matrix[V][i] == 1 and visited[i] == 0):
			dfs(i)


dfs(V)
print()
bfs(V)