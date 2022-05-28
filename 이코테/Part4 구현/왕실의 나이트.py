input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [[-2,-1],[-2,1],[2,-1], [2,1], [-1,-2],[-1,2],[1,-2],[1,2]]
count = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    print(step) #이중 리스트 안에 리스트만 나옴
    # [-2,-1]이런식으로
    print('next_row,next_column',next_row,next_column)

    if next_row < 1 or next_column < 1 or next_row > 8 or next_column > 8:
        
        #print('x')
        continue
    count+=1
print(count)