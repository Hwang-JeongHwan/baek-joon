a1 = [3] * 8
a2 = [3 for i in range(8)]
print('a1',a1)
print('a2',a2)

b1 = [*range(8)]
b2 = [i for i in range(8)]
print('b1',b1)
print('b2',b2)

c = [i+10 for i in range(8)]
print('c',c)

d = [i ** 2 for i in range(8)]
print('d',d)


e1 = [[1] * 4] * 3 #주의 ! 이 방식으로 다차원 리스트 생성은 지양할것
e2 = [[1] * 4 for _ in range(3)]
e3 = [[1 for _ in range(4)]for _ in range(3)]
print('e1',e1)
print('e2',e2)
print('e3',e3)