import math
import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
        
    print(math.comb(y, x))
