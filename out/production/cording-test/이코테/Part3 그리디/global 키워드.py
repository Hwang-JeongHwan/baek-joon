# global 키워드로 변수를 지정하면 해당 함수에서는 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를
# 바로 참조하게됨

# 함수 바깥쪽에 있는 변수를 참조하려면 global키워드를 사용해야함 

a = 0
b = 0
def func():
    global a 
    a += 1
    #b += 1 # 이건 안됨

for i in range(10):
    func()

print(a) 

array = [1, 2, 3, 4, 5]
def func1():
    array.append(6) # 전역변수로 리스트가 선언되어있을때 리스트의 내부 메소드를 호출하는것은 오류없이 가능
    print(array)

def func2():
    array = [3, 4, 5] # 지역변수와 전역변수가 동일한 이름으로 선언 되어있는 경우 함수안에 있는 지역변수를
    # 참조함 
    array.append(6)
    print(array)
func1()

func2()
print(array)

# 실제 코딩테스트에서는 어떠한 리스트 객체는 단순히 전역변수로 사용하는 경우가 많고
# 함수에서도 해당 변수를 바로 참조하도록 만드는경우가 많기 때문에
# 두개이상의 변수가 동일한 이름을 가지는게 아니라면 위와같이 신경쓸일이 많지 않음
# 전역변수를 참조할때는 global키워드를 사용

def func3():
    global array
    array = [3, 4, 5]
    array.append(6)

func3()
print(array) # 이렇게하면 3,4,5,6출력 전역변수에 있는 값을 참조해서 값을 변경하거나 해야할때는 global키워드
# 사용해야함 