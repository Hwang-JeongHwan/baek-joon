# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
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

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화 하기

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기

for i in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬 하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    # 튜플의 원소가 여러개면 첫 번째 원소 기준으로 정렬
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    # 해당 간선에 포함되어있는 두 원소 a와 b에 대해 이미 같은 집합에 속하지 않으면 합치기 연산을 수행
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        # 연산을 수행할때마다 result값에 비용을 더해줌 
        result += cost

print(result)