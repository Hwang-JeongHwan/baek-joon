# 반복문에서 남은 코드의 실행을 건너뛰고, 다음 반복을 진행하고자 할 때 continue를 사용함
# 1부터 9까지의 홀수의 합을 구할때 다음과 같이 작성할수 있음
result = 0
for i in range(1, 10):
    if i % 2 == 0:
        continue # continue 밑의 코드를 무시하고 다음 반복을 진행함 
    result += i
print(result)