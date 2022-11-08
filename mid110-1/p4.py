N = int(input())

data = []
enemy = []
win = []
lose = []

for i in range(N):
    data.append(input().split())
    data[i][2] = int(data[i][2])
    data[i][3] = int(data[i][3])

for e in data:
    flag = 0
    record = -1 
    for i in range(len(enemy)):
        if e[0] == enemy[i]:
            flag = 1
            record = i
            break
    if flag == 1:
        if e[1] == 'H':
            if e[2] > e[3]:
                win[record] += 1
            elif e[3] > e[2]:
                lose[record] += 1
        elif e[1] == 'A':
            if e[2] > e[3]:
                lose[record] += 1
            elif e[3] > e[2]:
                win[record] += 1
    else: # flag == 0
        enemy.append(e[0])
        if e[1] == 'H':
            if e[2] > e[3]:
                win.append(1)
                lose.append(0)
            elif e[3] > e[2]:
                lose.append(1)
                win.append(0)
        elif e[1] == 'A':
            if e[2] > e[3]:
                lose.append(1)
                win.append(0)
            elif e[3] > e[2]:
                win.append(1)
                lose.append(0)

for i in range(len(enemy)):
    print("vs.", enemy[i], "勝率：", round( win[i] / ( win[i]+lose[i] ), 1 ) )
