'''
문제설명
한 마을은 N개의 집과 M개의 도로로 구성되어 있다. 각 집은 0~N-1번까지의 번호로 구분된다. 모든 도로에는 가로등이 구비되어 있는데, 특정한 도로의 가로등을 하루 동안 켜기 위한 비용은 해당 도로의 길이와 동일하다. 예를 들어, 2번과 3번 집 사이를 연결하는 길이가 7인 도로가 있다고 가정하자. 하루 동안 이 가로등을 켜기 위한 비용은 7이 된다. 

정부에서는 일부 가로등을 비활성화하되, 마을에 있는 임의의 두 집에 대하여 가로등이 켜진 도로만으로도 오갈 수 있도록 만들고자 한다. 결과적으로 일부 가로등을 비활성하여 최대한 많은 금액을 절약하고자 한다. 마을의 집과 도로 정보가 주어졌을 때, 일부 가로등을 비활성화하여 절약할 수 있는 최대 금액을 출력하는 프로그램을 작성해라.

입력조건
첫째 줄에 집의 수 N( 1<= N <= 200,000)과 도로의 수 M(N-1 <= M <= 200,000)이 주어진다.
다음 M개의 줄에 걸쳐서 각 도로에 대한 정보 X,Y,Z가 주어지며 공백으로 구분된다.(0 <= X,Y <= N) 이는 X번 집과 Y번 집 사이에 양방향 도로가 있으며, 그 길이가 Z라는 의미이다. 단, X와 Y가 동일한 경우는 없으며 마을을 구성하는 모든 도로의 길이 합은 
2
31
보다 작다.
출력조건
첫째 줄에 일부 가로등을 비활성화하여 절약할 수 있는 최대 금액을 출력한다.'''

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

# 양방향 그래프
n, m = map(int, input().split())
parent = [0] * n
result = 0
edges = []
total = 0
for i in range(n):
    parent[i] = i

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
    total += cost

edges.sort()
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(total - result)