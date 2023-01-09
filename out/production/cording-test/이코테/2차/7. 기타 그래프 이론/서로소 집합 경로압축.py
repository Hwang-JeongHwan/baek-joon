# 찾기(Find) 함수를 최적화 하기 위한 방법으로 경로 압축(Path Compression)을 이용할수 있습니다.
# 찾기(Find) 함수를 재귀적으로 호출한 뒤에 부모 테이블 값을 바로 갱신합니다.

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
        # print(parent[x])
        # find함수를 호출한 뒤에 부모테이블에 적혀있는 부모의 값이 자신의
        # 루트가 되도록 설정
        # find연산을 수행한 뒤에는 부모테이블의 값이 다시 루트가 되도록
        # 하여 find함수를 호출할때 사용했던 부모의 값이 루트가 되도록함
        # 현재노드가 루트 노드가 아닐때 재귀적으로 그 부모에 대해서도 find_parent
        # 함수를 호출한 뒤에 그렇게 반환된 루트노드에 대한 값이
        # 부모테이블에 담길수 있도록하여 경로를 압축 

    return parent[x]
# 경로 압축 기법을 적용하면 각 노드에 대하여 찾기(Find) 함수를 호출한 이후에
# 해당 노드의 루트가 바로 부모 노드가 됩니다.

# 동일한 예시에 대해서 모든 합집합(Union) 함수를 처리한 후 각 원소에 대하여 찾기(Find)
# 함수를 수행하면 다음과 같이 부모 테이블이 갱신됩니다.
# 기본적인 방법에 비하여 시간 복잡도가 개선됩니다.

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i
# print(parent)
for i in range(e):
    a, b = map(int, input().split())
#    print(a, b)
    union_parent(parent, a, b)

# 각 원소가 속한 집합
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블의 내용
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')

