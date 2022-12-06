from itertools import combinations
tc = int(input())
for t in range(1, tc + 1):
    n, l = map(int, input().split())
    data = []
    for i in range(n):
        a, b = map(int, input().split())
        data.append((a, b))
    
    
    result = []
    for c in range(1, n + 1):
      
        for combi in combinations(data, c):
            score = 0
            cal = 0
            for i, j in combi:
                score += i
                cal += j
                # print(c, score, cal)
            if cal <= l:
                result.append(score)
    
    print('#{} {}'.format(t, max(result)))
