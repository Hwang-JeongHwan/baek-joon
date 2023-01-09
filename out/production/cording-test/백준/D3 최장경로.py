# def dfs(v, count):
#     global result
#     result = max(result, count)

#     visited[v] = True

#     for i in range(1, n + 1):
#         if visited[i] == False:
#             if data[v][i] == 1:
#                 dfs(i, count + 1)
    





# tc = int(input())
# for t in range(1, tc + 1):
#     n, m = map(int, input().split())
#     data = [[0] * (n + 1) for _ in range(n + 1)]
#     for _ in range(m):
#         a, b = map(int, input().split())
#         data[a][b] = 1
#         data[b][a] = 1

#     visited = [0] * (n + 1)
#     result = 1
#     for i in range(1, n + 1):
#         if visited[i] == False:
#             dfs(i, 1)
#     print(result)

# def dfs(v, count):
#     global result
#     result = max(result, count)
#     visited[v] = True
#     for i in range(1, n + 1):
#         if visited[i] == False:
#             if graph[v][i] == 1:
#                 dfs(i, count + 1)
#                 visited[i] = 0


# tc = int(input())
# for t in range(1, tc + 1):
#     n, m = map(int, input().split())
#     graph = [[0] * (n + 1) for _ in range(n + 1)]
#     for _ in range(m):
#         a, b = map(int, input().split())
#         graph[a][b] = 1
#         graph[b][a] = 1

    
#     result = 1
    
#     for i in range(1, n + 1):
#         visited = [False] * (n + 1)
        
#         dfs(i, 1)
    
#     print('#{} {}'.format(t, result))

def dfs(v, count):
    global result
    result = max(result, count)
    for i in graph[v]:
        if visited[i] == False:
            visited[i] = True
            dfs(i, count + 1)
            visited[i] = False

tc = int(input())
for t in range(1, tc + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].appned(b)
        graph[b].append(a)

    
    result = 1
    visited = [False] * (n + 1)
            
    for i in range(1, n + 1):
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0

    print('#{} {}'.format(t, result))