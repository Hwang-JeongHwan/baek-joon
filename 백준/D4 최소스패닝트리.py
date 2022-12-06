
# 크루스칼 알고리즘 : 대표적인 최소신장 트리 알고리즘 입니다
# 그리디 알고리즘으로 분류 됩니다.

# 구체적인 동작과정은 다음과 같습니다
# 1. 간선 데이터를 비용에 따라 오름차순으로 정렬합니다.
# 2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인합니다.
# 1) 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킵니다.
# 2) 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않습니다.
# 3. 모든 간선에 대하여 2번의 과정을 반복합니다.
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
tc = int(input())
for t in range(1, tc + 1):
    # 노드의 개수와 간선(Union 연산)의 개수 입력받기
    v, e = map(int, input().split())
    parent = [0] * (v + 1)

    # 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
    edges = []
    result = 0

    # 부모 테이블상에서, 부모를 자기 자신으로 초기ㅗ하
    for i in range(1, v + 1):
        parent[i] = i

    for _ in range(e):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))

    edges.sort()

    for edge in edges:
        cost, a, b = edge
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
    print('#{} {}'.format(t, result))