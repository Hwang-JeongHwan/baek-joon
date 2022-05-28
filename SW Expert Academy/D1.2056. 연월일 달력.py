# 2 => 28
# 4 6 9 11  30 
# 1 3 5 7 8 10 12
# 00 13

# 4 5
t = int(input())
answers = []

def check_YMD(year, month, day):
    day_list = [32, 29, 32, 31, 32, 31, 32, 32, 31, 32, 31, 32]

    if int(year) < 0 :
        return False

    if int(month) not in range(1, 13):
        return False
    
    if int(day) not in range(1, day_list[int(month) - 1]):
        return False
    return True

    
for _ in range(t):
    array = input()
    year = array[:4]
    month = array[4:6]
    day = array[6:]

    if check_YMD(year, month, day):
        answer = '/'.join([year, month, day])
    else:
        answer = -1

    answers.append(answer)

for i in range(t):
    # print(f"#{i + 1} {answers[i]}")
    print('#{} {}'.format(i + 1, answers[i]))

