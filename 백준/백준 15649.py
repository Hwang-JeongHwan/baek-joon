def dfs(i, count):
    visited[i] = True
    if count == m:
        print(*stack)
        return
    for i in range(1, n + 1):
        if visited[i] == False:
            stack.append(i)
            dfs(i, count + 1)
            stack.pop()
            visited[i] = False




n, m = map(int, input().split())
stack = []
visited = [False] * (n + 1)
dfs(0, 0)