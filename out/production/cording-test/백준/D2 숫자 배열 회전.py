

# 회전 전의 열번호 = 회전후의 행 번호
# 회전 후의 열 번호 = n - 1 - 회전전의 행번호

# n = 3
# before        after
# (0, 0)        (0, 2) graph[a][b] = graph[b][n - 1 - a]
# (0, 1)        (1, 2) graph[a][b] = graph[b][n - 1 - a]
# (1, 0)        (0, 1) 
'''
def rotate_2d(list_2d):
    n = len(list_2d) # 행 길이 계산
    m = len(list_2d[0]) # 열 길이 계산
    new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[j][n-i-1] = list_2d[i][j]
    return new
 

180도 회전

90도 회전을 두 번 하는 것이니, [j] 열 입장에서도 사이클이 생긴다.

def rotate_2d(list_2d):
    n = len(list_2d) # 행 길이 계산
    m = len(list_2d[0]) # 열 길이 계산
    new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[m-j-1][n-i-1] = list_2d[i][j]
    return new
 

270도 회전

90도 회전을 세 번 하는 것인데, 즉 -90도 회전하는 것과도 같다. 또는 180 + 90도 회전으로 이해할 수 있다.

def rotate_2d(list_2d):
    n = len(list_2d) # 행 길이 계산
    m = len(list_2d[0]) # 열 길이 계산
    new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[m-j-1][i] = list_2d[i][j]
    return new
    '''

def rotate_90(graph):
    n = len(graph)
    m = len(graph[0])
    new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[j][n - i - 1] = graph[i][j]

    return new
tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    rotate90 = rotate_90(graph)
    rotate180 = rotate_90(rotate90)
    rotate270 = rotate_90(rotate180)
    #print(rotate90,rotate180,rotate270)
    print('#{}'.format(t))
    for i in range(n):
        print(''.join(map(str, rotate90[i])), end=' ')
        print(''.join(map(str, rotate180[i])), end=' ')
        print(''.join(map(str, rotate270[i])), end =' ')
        print()

def rotate(graph):
    n = len(graph)
    m = len(graph[0])
    new = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            new[j][n - i -1] = graph[i][j]

    return new
