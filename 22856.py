#트리 순회
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())
tree = {}
parent = [0] * (N + 1)
movement = 0

class Node:
	def __init__(self, data, left, right):
		self.data = data
		self.left = left
		self.right = right

for _ in range(N):
    a, b, c = map(int, input().split())
    tree[a] = Node(a, b, c)

def in_order(node):
    if node.left != -1:
        in_order(tree[node.left])
    parent.append(node.data)
    if node.right != -1:
        in_order(tree[node.right])


def similar_in_order(node):
    global movement

    if node.left != -1:
        similar_in_order(tree[node.left])
        movement += 1

    if node.data == parent[-1] :
        print(movement)
        exit(0)
	#왼쪽 다 가면 올라와야하니까
    movement += 1

    if node.right != -1:
        similar_in_order(tree[node.right])
        movement += 1

in_order(tree[1])
similar_in_order(tree[1])