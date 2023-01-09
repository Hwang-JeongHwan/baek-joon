from itertools import combinations
tc = int(input())
for t in range(1, tc + 1):
    n, b = map(int, input().split())
    data = list(map(int, input().split()))
    
    result = []
    for i in range(1,n + 1):
        for combi in combinations(data, i):
            total = sum(combi)
            
            if total >= b:
                result.append(total - b)
    answer = min(result)
    print('#{} {}'.format(t, answer))