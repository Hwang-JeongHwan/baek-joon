# 특정 원소가 속한 집합을 찾기

def find_parent(parent, x):
   # print('x', x)
    # 루트 노드를 찾을 때 까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x]) # 재귀적으로 호출해서 나온값을 return
    return x

# while True:  
#     if parent[x] != x:
#         x = parent[x]
#     else:break

# 두 원소가 속한  집합을 합치기
def union_parent(parent, a, b):
    # print('b',parent[a], parent[b])
    # print('before find',a, b)
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # print('after find', a, b)
    if  a < b:
        parent[b] = a
    else: # 작거나 같은 경우 낮은번호로 
        parent[a] = b
    # print('a', parent[a], parent[b])


# 노드의 개수와 간선(Union 연산)의 개수 입력받기
v , e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화 하기

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# Union 연산을 각각 수행

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기 = 각 노드의 루트노드 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i) , end=' ')

print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')

# 서로소 집합 자료구조: 기본적인 구현 방법의 문제점
# 합집합 연산이 편향되게 이루어지는 경우 찾기 함수가  비효율적으로 동작합니다.

# 최악의 경우에는 찾기 함수가 모든 노드를 다 확인하게 되어 시간 복잡도가 O(V)입니다.

# 다음과 같이 {1, 2, 3, 4, 5}의 총 5개의 원소가 존재하는 상황을 확인해 봅시다

# 수행된 연산들 Union(4, 5), Union(3, 4), Union(2, 3), Union(1, 2)

# 1 <- 2 <- 3 <- 4 <- 5 
# 노드번호 1    2   3   4   5
# 부모      1   1   2   3   4
