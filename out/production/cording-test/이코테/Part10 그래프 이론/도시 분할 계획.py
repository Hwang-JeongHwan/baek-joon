# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력받기
n, m = map(int, input().split())
# 부모 테이블 초기화
parent = [0] * (n + 1)

# 모든 부모노드를 자기 자신으로 설정
for i in range(1, n + 1):
    parent[i] = i
# 모든 간선 정보를 담을 리스트와, 최종 비용을 담을 변수 
edges = []
result = 0

for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
    
# 간선 비용순으로 정렬
edges.sort()
last = 0 # 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선

# 간선을 하나씩 확인하며
for edge in edges:
    c, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함 
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        print(c)
        result += c
        last = c

print(result - last)

