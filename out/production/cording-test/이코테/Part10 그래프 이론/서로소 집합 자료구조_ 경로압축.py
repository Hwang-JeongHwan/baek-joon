# 찾기 함수를 최적화 하기위해 경로 압축(Path Compression)을 이용할수 있음
# 찾기(Find)함수를 재귀적으로 호출한 뒤에 부모 테이블 값을 바로 갱신합니다.
# 특정 원소가 속한 집합을 찾기
# 루트노드 까지 도달하기 위한 경로를 압축 
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        # 자신의 부모값이 될수있도록 갱신
        # 결과적으로 find함수를 호출한 뒤에 부모테이블에 적혀있는 부모의 값이 자신의 루트가 될수있도록 설정
        # find함수를 수행한 뒤에는 부모테이블의 값이 다시 루트가 될수있도록 하여 find함수를 호출 할 때 사용했던
        # 노드에 대한 부모의 값이 루트와 동일하도록 경로가 압축됨 
        parent[x] = find_parent(parent, parent[x])

    return parent[x]



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