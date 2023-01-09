# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x): # parent = 부모 테이블,  x = 노드번호
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        # 루트노드를 찾기 위해 자신의 부모노드의 번호를 넣어서 다시한번 find_parent 함수를 호출
        return find_parent(parent, parent[x])
    
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    # a와b의 루트 번호를 찾은뒤에 각각의 루트번호를 확인해서 큰쪽이 작은쪽의 루트번호를 부모로 설정 
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자신으로 초기화
for i in range(1,v + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a , b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ',end =' ')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')
print()

# 부모 테이블 내용 출력
# 부모 테이블은 자신의 부모에 대한 정보를 가지고 있으며, 이 값이 자신의 루트 즉 집합에 대한 정보가 아닐수있다는것을 유의 
print('부모 테이블: ', end =' ')
for i in range(1, v + 1):
    print(parent[i],end=' ')