N = int(input())

while N > 10 or N < 1:
    print("Error! N is out of range!")
    print("N must be in range 1 - 10")
    N = int(input())
A = [0, 0, 0, 0]
B = [0, 0, 0, 0]
C = [0, 0, 0, 0]
D = [0, 0, 0, 0]

for i in range(N):
    data = [ e for e in input().split() ]
    for i in range(len(data)-1):
        if data[i] == '直':
            if data[i+1] == '直':
                A[0] += 1
            elif data[i+1] == '滑':
                A[1] += 1
            elif data[i+1] == '伸':
                A[2] += 1
            elif data[i+1] == '曲':
                A[3] += 1
        elif data[i] == '滑':
            if data[i+1] == '直':
                B[0] += 1
            elif data[i+1] == '滑':
                B[1] += 1
            elif data[i+1] == '伸':
                B[2] += 1
            elif data[i+1] == '曲':
                B[3] += 1
        elif data[i] == '伸':
            if data[i+1] == '直':
                C[0] += 1
            elif data[i+1] == '滑':
                C[1] += 1
            elif data[i+1] == '伸':
                C[2] += 1
            elif data[i+1] == '曲':
                C[3] += 1
        elif data[i] == '曲':
            if data[i+1] == '直':
                D[0] += 1
            elif data[i+1] == '滑':
                D[1] += 1
            elif data[i+1] == '伸':
                D[2] += 1
            elif data[i+1] == '曲':
                D[3] += 1

target = input()

if target == '直':
    print('直', A[0], '/', sum(A))
    print('滑', A[1], '/', sum(A))
    print('伸', A[2], '/', sum(A))
    print('曲', A[3], '/', sum(A))
elif target == '滑':
    print('直', B[0], '/', sum(B))
    print('滑', B[1], '/', sum(B))
    print('伸', B[2], '/', sum(B))
    print('曲', B[3], '/', sum(B))
elif target == '伸':
    print('直', C[0], '/', sum(D))
    print('滑', C[1], '/', sum(D))
    print('伸', C[2], '/', sum(D))
    print('曲', C[3], '/', sum(D))
elif target == '曲':
    print('直', D[0], '/', sum(D))
    print('滑', D[1], '/', sum(D))
    print('伸', D[2], '/', sum(D))
    print('曲', D[3], '/', sum(D))
