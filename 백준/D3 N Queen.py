def dfs(depth):
    global result
    # print('fd',depth)
    if depth == n + 1:
        result += 1
        return

    for i in range(1, n + 1):

        data[depth] = i
        # print('depth',depth,i)

        flag = True
        for j in range(1, depth):
            if data[depth] == data[j] or abs(data[depth] - data[j]) == depth - j:
                flag = False
                break

        if flag:
            if not visited[i]:
                # print('f',i)
                visited[i] = True
                dfs(depth + 1)
                visited[i] = False


def check(depth):
    for i in range(1, depth):
        if data[depth] == data[i] or abs(data[depth] - data[i]) == depth - i:
            return False
    return True


tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    data = [0] * (n + 1)
    visited = [0] * (n + 1)
    result = 0
    dfs(1)
    print('#{} {}'.format(t, result))
