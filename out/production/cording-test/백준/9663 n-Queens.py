def dfs(depth):
    global count 
    if depth == n : # n번째 까지 갔으면
        count += 1
        return

    for i in range(n):
        if visited[i] == 0: # 아직 방문하지 않았다면
            graph[depth] = i # 그래프의 해당 깊이에 퀸을 둬봄 
            if promising(depth): # 유망하다면
                visited[i] = 1 # 방문처리후
                dfs(depth + 1) # 다음 깊이를 탐색
                visited[i] = 0 # 탐색이 끝나고 난뒤 백트래킹

def promising(depth):
    for i in range(depth): 
        # 같은 열에 있거나              같은 대각선에 있다면
        if graph[depth] == graph[i] or abs(graph[depth] - graph[i]) == depth - i:
            return False # False 반환

    return True 




n = int(input())
graph = [0] * n # 퀸의 정보를 담을 배열
visited = [0] * n # 방문여부 check
count = 0 # 전체 개수

dfs(0)
print(count)