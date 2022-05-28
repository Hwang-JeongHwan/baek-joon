def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
# 부모테이블 초기화
parent = [0] * (n + 1)
# 부모 테이블상에서 모든 학생의 부모노드를 자기 자신으로 초기화
for i in range(0, n + 1):
    parent[i] = i

for i in range(m):
    x, a, b = map(int, input().split())
    # 합집합(union) 연산인 경우
    if x == 0:
        union_parent(parent, a, b)
    # 찾기(find) 연산인 경우
    elif x == 1:
        if find_parent(parent,a) == find_parent(parent,b):
            print('YES')
        else:
            print('NO')

