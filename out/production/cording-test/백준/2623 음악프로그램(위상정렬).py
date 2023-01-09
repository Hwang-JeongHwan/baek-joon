from collections import deque
def topology_sort(data):
    q = deque(data)
    flag = True
    for i in range(1, n + 1):
        if len(q) == 0:
            flag = False
            break

        now = q.popleft()
        # print(now)
        result.append(now)
        for j in graph[now]:
            indegree[j] -= 1
            if indegree[j] == 0:
                q.append(j)
    return flag

n, m = map(int, input().split())
data = []
result = []
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    array = list(map(int, input().split()))
    for i in range(1, array[0]):
        graph[array[i]].append(array[i + 1])
        indegree[array[i + 1]] += 1
# print(graph)

for i in range(1, n + 1):
    if indegree[i] == 0:
        data.append(i)

if topology_sort(data):
    for i in range(n):
        print(result[i])
else:
    print(0)

