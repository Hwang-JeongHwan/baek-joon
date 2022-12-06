# 1, 2 동, 서 = 세로
# 3, 4 남,북 = 가로

# 2, 160 가장긴거
# 4, 50 가장긴거

n = int(input())
data = []
max_width = 0
max_width_index = 0
max_height = 0
max_height_index = 0
for _ in range(6):
    x, y = map(int, input().split())
    data.append((x, y))

for i in range(6):
    if data[i][0] == 1 or data[i][0] == 2:
        if max_height < data[i][1]:
            max_height = data[i][1]
            max_height_index = i

    elif data[i][0] == 3 or data[i][0] == 4:
        if max_width < data[i][1]:
            max_width = data[i][1]
            max_width_index = i


total = max_height * max_width

small_height = abs(data[(max_height_index + 1) % 6][1] - data[(max_height_index - 1) % 6][1])
small_width = abs(data[(max_width_index + 1) % 6][1] - data[(max_width_index - 1) % 6][1])

print(n * (total - (small_height * small_width)))
