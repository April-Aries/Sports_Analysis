data = [ int(e) for e in input().split() if int(e) < 100 ]

if len(data) == 0:
    print("Error! No input!")
else:
    average_data = sum(data) / len(data)
    range_data = max(data) - min(data)
    if average_data >= 10:
        if range_data >= 10:
            print("表現優異 起伏過大")
        elif 10 > range_data >= 5:
            print("表現優異 尚稱穩定")
        elif range_data < 5:
            print("表現優異 相當穩定")
    elif 10 > average_data >= 5:
        if range_data >= 10:
            print("表現平平 起伏過大")
        elif 10 > range_data >= 5:
            print("表現平平 尚稱穩定")
        elif range_data < 5:
            print("表現平平 相當穩定")
    elif average_data < 5:
        if range_data >= 10:
            print("表現不佳 起伏過大")
        elif 10 > range_data >= 5:
            print("表現不佳 尚稱穩定")
        elif range_data < 5:
            print("表現不佳 相當穩定")
    else:
        print("Error: Not match!")

