'''
https://www.acmicpc.net/problem/1922
'''

import sys
input = sys.stdin.readline

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

n = int(input())
m = int(input())
parent = [0] * (n + 1)

result = 0
edges = []
for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

# 크루스칼 알고리즘 성능 분석
# 크루스칼 알고리즘은 간선의 개수가 E개일 때, O(ElogE)의 시간복잡도를 가집니다
# 크루스칼 알고리즘에서 가장 많은 시간을 요구하는 곳은 간선을 정렬 수행하는 부분입니다.
# 표준 라이브러리를 이용해 E개의 데이터를 정렬하기 위한 시간 복잡도는 O(ElogE)입니다.
