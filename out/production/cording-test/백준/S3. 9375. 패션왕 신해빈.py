# 풀이 과정
# 같은 종류의 의상은 하나씩만 착용할 수 있으며, 알몸이 아니어야 하므로 꼭 1종류 이상의 의상은 착용해야 한다.

# 예를 들어, 3종류의 의상이 있으면 1종류만 착용해도 되며, 2종류를 착용해도 되고, 3종류를 착용해도 되지만

# 0종류를 착용하는건 안된다.

 

# 그렇다면 다음과 같은 식을 세울 수 있다.

# (a종류수 + 1) * (b종류수 + 1) * (c종류수 + 1)... - 1

 

# 여기서 종류수에 +1을 해준 이유는 그 종류의 의상을 착용해도 되고 안해도 되기 때문이고

# 마지막에 -1을 해준 이유는 모든 의상을 착용하지 않은 경우를 제외시켜줘야 하기 때문이다.

 

# 의상의 종류와 그 종류에 있는 의상 이름을 나타내기 위해 딕셔너리를 이용하였다.

t = int(input())

for i in range(t):
    n = int(input())
    weardict = {}
    for j in range(n):
        wear = list(input().split())
        if wear[1] in weardict:
            weardict[wear[1]].append(wear[0])
        else:
            weardict[wear[1]] = [wear[0]]

    cnt = 1 # 각 종류마다 항목의 개수

    for k in weardict:
        cnt *= (len(weardict[k])+1)
    print(cnt-1)