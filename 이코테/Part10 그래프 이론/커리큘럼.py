from collections import deque
import copy

#  노드 개수 입력 받기
v = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]
# 각 강의 시간을 0으로 초기화
time = [0] * (v + 1)


for i in range(1, v + 1):
    data = list(map(int, input().split()))
    time[i] = data[0] # 첫 번째 수는 시간 정보를 담고 있음
    for x in data[1:-1]: #x = [1,2,3,4,5] -> [2,3,4] 출력
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
    print('time',time)
    print('result',result)
    q = deque()

    # 처음 시작 할 때는 집입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

# 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        for i in graph[now]:
            # 현재시간 + time[i] // 각각 업데이트 해준다고 보면됨 -> 4번 강의(3분)가 3번 강의(4분)를 듣고 들어야하고
            # 3번 강의가 1번 강의(10)를 들어야하는경우 
            # 14 + 3 = 17 

            # max(원래 리스트에서 가지고 있던 시간 , 진입 노드가 0인 현재노드의 시간 + 처음 입력받은 시간)
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    for i in range(1, v +1):
        print(result[i])

topology_sort()