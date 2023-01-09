# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x,y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    # 현재 노드를 아직 방문 하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        #print('b',graph)
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        #print('a',graph)
        # 상, 하, 좌, 우에 대해 호출되는 내용들은 리턴값을 사용하지 않기 떄문에
        # 단순히 연결된 모든 노드에대해 방문처리를 수행하기 위한 목적으로 수행됨
        # 이 DFS는 한번 수행되면 해당 노드와 연결된 모든 노드들을 방문처리 할수 있게 하고
        # 해당 노드가 방문처리가 되었다면 즉 처음 방문하는 것이라면 그때만 result값을 증가
        # 한번 True를 반환하고 나서 메인의 반복문에서 방문햇던 노드가 들어오게되면 graph[x][y] !=0
        # 이므로 True 반환이 안됨 
        # 재귀적으로 호출함 함수들이 True를 반환해도 False를 반환해도 상관없음
         
        return True

    return False


n,m = map(int, input().split())

'''
x = list(123)
print(x)
이렇게 하면 ['1', '2', '3'] 출력
'''

'''
x = list(map(int,'123'))
print(x)
이렇게 하면 [1, 2, 3]
'''

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    #한줄을 입력받고 각 원소를 정수형으로 바꿔서 리스트로 만듬 


# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
# n * m 크기의 각 위치에서 DFS수행 
for i in range(n): 
    for j in range(m):
        #현재 위치에서 DFS 수행 
        #print('i,j',i,j,dfs(i,j))
        if dfs(i,j) == True:
            result += 1
print(result)

         