N = int(input())

while N > 10 or N < 1:
    print("Error! Number of games is out of range!")
    N = int(input())

for i in range(N):
    raw_data = [ int(e) for e in input().split() if int(e) < 100 ]
    data = []
    # patterns
    A = 0
    B = 0
    C = 0
    for e in raw_data:
        data.append( ( e/sum(raw_data) ) * 100 )
        if ( e/sum(raw_data) ) * 100 >= 50:
            A += 1
            B += 1
            C += 1
        elif ( e/sum(raw_data) ) * 100 >= 35:
            B += 1
            C += 1
        elif ( e/sum(raw_data) ) * 100 >= 25:
            C += 1
    # pattern check
    if C == 3:
        print("三巨頭")
    elif B == 2:
        print("雙星組合")
    elif A == 1:
        print("一夫當關")
    else:
        print("多點開花")
