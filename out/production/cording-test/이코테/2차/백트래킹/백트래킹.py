# 백트래킹
# 모든 경우의수를 확인해야 할때
# for문으로는 확인 불가한 경우(깊이가 달라질때)

# 순열: M개의 숫자에서n개를 뽑을때 순서 상관이있는 경우
# 3개의 숫자 에서 2개를 뽑을때
# (1, 2) (1, 3) (2, 1) (2, 3) (3, 1) (3, 2) 6가지 

for i in range(1, 4):
    for j in range(1, 4):
        if i != j :
            print(i, j)
# 이런식으로for 문으로 확인가능
# 백트래킹을 언제 사용하나
# m, n이 정확히 정해지지 않을때 => 깊이가 달라질때

# n = 이면 for문을 더이상 사용할수 없음


# 백트래킹 기법
# 상태 공간 트리를 깊이 우선탐색으로 탐색
# 방문중인 노드에서 더 하위 노드로 가면 해답이 없을 경우
# 해당 노드의 하위 트리를 방문하지 않고 부모노드로 되돌아감 (backtrack)

# 유망함 => 어떤 노드가 더 가면 해답이 나올것이낙

# 방문 중인 노드에서 하위노드가 해답을 발견할 가능성이 있으면 유망
# 하위 노드에서 해답을 발견할 가능성이 없으면 유망하지 않음

# 백트래킹과 가지치기

# 백트래킹: 상태공간 트리를 DFS로 탐색
# 방문중인 노드가 유망한지 체크
# 만약 유망하지 않으면 부모 노드로 되돌아감

# 가지치기
# 유망하지 않으면 하위트리를 가지치기함
# 가지치기한 상태 : 방문한 노드의 방문하지 않는 하위 트리 
# def checknode(v):
#     if promising(v): 유망한 노드면 , 즉 하위 노드에 해답이 있을가능성이 있다면
#         if (v 에 해답이 있으면):
#             해답을 출력
#         else:
#             for (v의 모든 자식 노드에 대해서):
#                 checknode(v)
#     

# 백트래킹 알고리즘의 구현
# 상태 공간 트리를 실제로 구현할 필요는 없음
# 현재 조사중인 가지의 값에 대해 추적만 하면됨
# 상태공간트리는 암묵적으로 존재한다고 이해하면 됨
