from itertools import combinations

import sys

input = sys.stdin.readline

result = 100000
N = int(input())
l = []
for i in range(N):
    l1 = list(map(int,input().split()))
    l.append(l1)

member = [i for i in range(N)]


team_combi = []

for i in combinations(member,N//2):
    team_combi.append(i)


# print(team_combi)

for i in range(len(team_combi)//2):
    team_start = list(team_combi[i])
    team_link = list(set(member)-set(team_combi[i]))
    #차집합을 구함 
    # print('team_start',team_start)
    # print('team_link',team_link)

    start_hap = 0
    for i in range(len(team_start)):
        for j in team_start:
            start_hap += l[team_start[i]][j] #이렇게 해야 
            # 이차원 리스트에서 0,0 0,1 1,0 1,1 더할수있음
            # l[i][i]는 항상 0이므로 !
            # print('team_start[i]',team_start[i])
            # print('j',j)
            # print('l[team_start[i]][j]',l[team_start[i]][j])
            # print(start_hap)
    
    link_hap = 0 
    for i in range(len(team_link)):
        for j in team_link:
            link_hap +=l[team_link[i]][j]

    
    result = min(result,abs(start_hap - link_hap))
print(result)