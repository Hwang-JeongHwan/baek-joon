tc = int(input())
data = []
for t in range(1, tc + 1):
    a, b, c, d = map(int, input().split())

    alice = a/b
    bob = c/d
    if alice < bob:
        answer = 'BOB'
    elif alice > bob:
        answer = 'ALICE'
    else:
        answer = 'DRAW'
    data.append(answer)

for t in range(tc):
    print('#{} {}'.format(t + 1, data[t]))