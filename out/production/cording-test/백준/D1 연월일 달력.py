months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
days = ['31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']

tc = int(input())

for t in range(1, tc + 1):
    data = input()
    year = data[ : 4]
    month = data[4 : 6]
    
    day = data[6:]
    # print(month, day)

    if month in months :
        index = months.index(month)
        if int(day) <=  int(days[index]):
            print('#{} {}/{}/{}'.format(t, year, month, day))
        else:
            print('#{} -1'.format(t))
    else:
        print('#{} -1'.format(t))
