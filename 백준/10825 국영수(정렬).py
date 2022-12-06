# 국어점수 감소
# 국어점수가 같으면 영어점수 증가
# 국어점수와 영어점수가 같으면 수학점수 감소
# 모든 점수가 같으면 이름이 사전순으로
import sys
input = sys.stdin.readline
n = int(input())
data = []
for i in range(n):
    data.append(input().rstrip().split()) # key = lambda x : 여러개의 조건을 넣으려면
    #x: 뒤를 ()로 감싸주어야하고 내림차순으로 정렬하려면 -를 붙여줘야함
print(data)
data.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
    print(data[i][0])