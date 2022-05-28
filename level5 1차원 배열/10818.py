'''
문제
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

출력
첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

'''
'''
import sys
N = int(input())
min = 1000000
max = 0
a = list(map(int, sys.stdin.readline().split())) #리스트 형식으로 입력받기

for i in range(N):
    if(a[i]<min):
        min = a[i]
    if(a[i]>max):
        max = a[i]

print(min,max)
제대로 값이 출력되는데 틀렷다고 나옴;; 파이썬은 리스트의
min,max를 구할수있는 함수가 있어서 그거쓰면 된다고함

''' 

N = int(input())
a = list(map(int, input().split()))
print(min(a),max(a))