n, m = map(int, input().split())
graph = []
for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)

# print(graph)
home = []
chicken = []
min_d = []
max = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append((i, j))
        if graph[i][j] == 2:
            chicken.append((i, j))


# print('home',home)
# print('chicken',chicken)

# for i in home:
#     a, b = i
#     max_value = 0
#     for j in chicken:
#         x, y = j
#         if max_value < abs(x - a) + abs(y - a):
#             max_value = abs(x - a) + abs(y - a)
#             x_index, y_index = x, y
#     max.append([x_index,y_index])
for i in chicken:
    a, b = i
    hap = 0
    for j in home:
        x, y = j
        hap += abs(x - a) + abs(y - b)
    max.append((hap, a, b))

max.sort()
# print('max',max)
so = []
# print(max[0])    
for i in range(m):
    x, y, z = max[i]
    so.append((y,z))
# print(so)
for i in home:
    a, b = i
    min_value = 1e9

    for j in so:
        x, y = j
        min_value = min(min_value,abs(x - a) + abs(y - b))

    min_d.append(min_value)

print(sum(min_d))