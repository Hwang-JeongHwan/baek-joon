tc = int(input())

def dfs(depth):
    global count
    if depth == n:
        count += 1
        return
    for i in range(n):
        if visited[i] == 0:
            graph[depth] = i

            flag = True
            for j in range(depth):
                if graph[depth] == graph[j] or abs(graph[depth] - graph[j]) == depth - j:
                    flag = False
                    break
            if flag == True:
                visited[i] = 1

                dfs(depth + 1)
                visited[i] = 0
for t in range(1, tc + 1):
    n = int(input())
    graph = [0] * n
    visited = [0] * n
    count = 0
    dfs(0)
    print('#{} {}'.format(t, count))