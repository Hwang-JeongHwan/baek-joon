'''
[문제]
선생님은 시험을 본 학생 N명의 성적을 분실하고, 성적을 비교한 결과의 일부만 가지고 있습니다.

 

학생 N명의 성적은 모두 다른데, 다음은 6명의 학생에 대하여 6번만 성적을 비교한 결과입니다.

1번 학생의 성적 < 5번 학생의 성적
3번 학생의 성적 < 4번 학생의 성적
4번 학생의 성적 < 2번 학생의 성적
4번 학생의 성적 < 6번 학생의 성적
5번 학생의 성적 < 2번 학생의 성적
5번 학생의 성적 < 4번 학생의 성적
A번 학생의 성적이 B번 학생보다 낮다면 화살표가 A에서 B를 가리키도록 할 때 위의 성적 결과를 다음 그림처럼 표현할 수 있습니다.


정확한 순위
이 그림으로 유추해서 순위를 정확히 알 수 있는 학생도 있고, 알 수 없는 학생도 있습니다. 예를 들어 1번 학생은 5번 

 

학생보다 성적이 낮고, 5번 학생은 4번 학생보다 성적이 낮으므로 1번 학생은 4번 학생보다 성적이 낮습니다. 따라서

 

1번, 3번, 5번 학생은 모두 4번 학생보다 성적이 낮다고 볼 수 있습니다. 그리고 4번 학생은 2번 학생과 6번 학생보다

 

성적이 낮습니다. 정리하면 4번 학생보다 성적이 낮은 학생은 3명이고, 성적이 높은 학생은 2명이므로 4번 학생의 성적

 

순위를 정확히 알 수 있습니다. 하지만 예시에서 4번 학생을 제외한 다른 학생은 정확한 순위를 알 수 없습니다.

 

학생들의 성적을 비교한 결과가 주어질 때, 성적 순위를 정확히 알 수 있는 학생은 모두 몇 명인지 계산하는 프로그램을 작성하세요.

 

[입력 조건]
1. 첫째 줄에 학생들의 수 N(2 <= n <= 500)과 두 학생의 성적을 비교한 횟수 M(2 <= M <= 10,000)이 주어집니다.

 

2. 다음 M개의 각 줄에는 두 학생의 성적을 비교한 결과를 나타내는 두 양의 정수 A와 B가 주어집니다.

   이는 A번 학생의 성적이 B번 학생보다 낮다는 것을 의미합니다.

 

[출력 조건]
첫째 줄에 성적 순위를 정확히 알 수 있는 학생이 몇 명인지 출력합니다.

<입력 예시>
6 6
1 5
3 4
4 2
4 6
5 2
5 4
<출력 예시>
1

'''
# A에서 B로 도달가능하다는 것은, A가 B보다 성적이 낮다는 의미
# A에서 B로 도달이 가능하거나 B에서 A로 도달 가능하면 성적 비교가 가능한것

# A에서 B로 도달이 불가능 하며, B에서 A로도 도달이 불가능 하면 성적 비교 결과를 
# 알수 없음 
n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            print('i, j',i, j)
            count += 1
    if count == n:
        result += 1
print(result)

