'''
1, 2, 0
4, 5, 0
3 + 4 = 7

https://www.acmicpc.net/problem/2887
'''
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


import sys
input = sys.stdin.readline

n = int(input())
parent = [0] * (n + 1)
edges = []
same = []

x_array = []
y_array = []
z_array = []
for i in range(1, n + 1):
    parent[i] = i 
    
# x, y, z 좌표를 각각 담아줌
for i in range(1, n + 1):
    x, y, z = map(int, input().split())
    x_array.append((x, i))
    y_array.append((y, i))
    z_array.append((z, i))

x_array.sort()
y_array.sort()
z_array.sort()
# 각각의 간선0마다의 차이를 edges에 담아줌
for i in range(1, n):
    edges.append((x_array[i][0] - x_array[i - 1][0], x_array[i][1], x_array[i - 1][1]))
    edges.append((y_array[i][0] - y_array[i - 1][0], y_array[i][1], y_array[i - 1][1]))
    edges.append((z_array[i][0] - z_array[i - 1][0], z_array[i][1], z_array[i - 1][1]))

edges.sort()
result = 0
#print(edges)
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)



