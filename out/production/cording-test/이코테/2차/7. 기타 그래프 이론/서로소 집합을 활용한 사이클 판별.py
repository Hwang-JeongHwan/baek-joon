# 서로소 지합은 무방향 그래프 내에서의 사이클을 판별할 때 사용할 수 있습니다.

# 참고로 방향그래프에서의 사이클 여부는 DFS를 이용하여 판별할 수 있습니다

# 사이클 판별 알고리즘은 다음과 같습니다

# 1. 각 간선을 하나씩 확인하며 두 노드의 루트 노드를 확인합니다
# 1) 루트 노드가 서로 다르다면 누 노드에 대하여 합집합(Union)연산을 수행합니다.
# 2) 루트 노드가 서로 같다면 사이클(Cycle)이 발생한 것입니다

# 2. 그래프에 포함되어있는 모든 간선에 1번 과정을 반복합니다.
# 서로소 지합은 무방향 그래프 내에서의 사이클을 판별할 때 사용할 수 있습니다.

# 참고로 방향그래프에서의 사이클 여부는 DFS를 이용하여 판별할 수 있습니다

# 사이클 판별 알고리즘은 다음과 같습니다

# 1. 각 간선을 하나씩 확인하며 두 노드의 루트 노드를 확인합니다
# 1) 루트 노드가 서로 다르다면 누 노드에 대하여 합집합(Union)연산을 수행합니다.
# 2) 루트 노드가 서로 같다면 사이클(Cycle)이 발생한 것입니다

# 2. 그래프에 포함되어있는 모든 간선에 1번 과정을 반복합니다.

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

v, e = map(int, input().split())
graph = []
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

cycle = False
for _ in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break

    else:
        
        union_parent(parent, a, b)
    
if cycle:
    print('사이클이 발생했습니다.')

else:
    print('사이클이 발생하지 않았습니다.')
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

v, e = map(int, input().split())
graph = []
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

cycle = False
for _ in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break

    else:
        
        union_parent(parent, a, b)
    
if cycle:
    print('사이클이 발생했습니다.')

else:
    print('사이클이 발생하지 않았습니다.')