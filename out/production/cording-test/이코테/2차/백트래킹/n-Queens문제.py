# n-Queens문제

# 8-Queens (n = 8) 문제의 일반화된 문제

# n x n 체스보드에 n개의 퀸을 배치하는 문제
# 어떤 퀸도 다른 퀸에 의해서 잡아먹히지 않도록 배치해야함
# 즉 같은행, 열, 대각선에는 다른 퀸을 놓을수 없음

# 백트래킹으로 문제 해결:
# 임의의 집합에서 기준에 따라 원소의 순서를 선택

# n-queens 문제에 적용:
# 임의의 집합(set) : 체스 보드에 있는 n^2개의 가능한 위치
# 기준: 새로 놓을 퀸이 다른 퀸을 위협할 수 없음
# 원소의 순서:퀸을 놓을수 있는 n개의 위치

# 4-Queen문제 n = 4
# 4개의 퀸을 4 x 4 체스보드에 배치
# 일단 기본 가정으로 같은 행(row)에 놓을수 없음
# 후보해답 4 x 4 x 4 x 4 = 256 가지의 탐색 공간이 있음

# 상태공간 트리의 구성

# n-Queens 문제의 해결
# 기본가정: 같은 행에는 퀸을 놓지 않는다
# 유망함수의 구현:
# 같은 열이나 같은 대각선에 놓이는지를 확인

# 유망의 조건 1: 같은 열 체크
# col[i]: i번째 행에 퀸이 놓여있는 열의 위치
# col[k]: k번째 행에서 퀸이 놓여있는 열의 위치
# col[i] == col[k] : 같은 열에 놓이게 되므로 유망하지 ㅇ낳다


# 유망의 조건 2: 대각선 체크
# col[6] - col[3] = 4 - 1 = 3 =  6 - 3
# col[6] - col[2] = 4 - 8 = -2 = 2 - 6


# 왼쪽에서 위협하는 퀸에 대해서 
# 열에서의 차이는 행에서의 차이와 같다
# col[i] - col[k] == i - k
# 오른쪽에서 위협하는 퀸에 대해서
# 열에서의 차이는 행에서의 차이의 마이너스와 같다
# col[i] - col[k] == k - i

# col[i] 와 col[k]의 절대값으로 대각선 위협 판단


def n_queens(i, col):
    n = len(col) - 1
    if promising(i, col):
        if i == n:
            print(col[i: n + 1])
        
        else:
            for j in range(1, n + 1):
                col[i + 1] = j
                n_queens(i + 1, col)


def promising(i, col):
    k = 1
    flag = True
    while k < i and flag:

        # 같은열에있거나        또는 같은 대각선에 있으면 
        if col[i] == col[k] or abs(col[i] - col[k]) == (i - k):
            flag = False
        k += 1
    return flag       

n = 4
col = [0] * (n + 1)
n_queens(0, col)