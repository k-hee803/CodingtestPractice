while True:
    side = list(map(int, input().split()))
    sorted_side = sorted(side)

    if sorted_side[2] == 0:
        break
    else:
        if sorted_side[2]**2 == sorted_side[0]**2 + sorted_side[1]**2:
            print('right')
        else:
            print('wrong')