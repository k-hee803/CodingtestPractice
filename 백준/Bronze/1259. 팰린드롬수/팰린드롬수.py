while True:
    num = input()
    reverse_num = num[::-1]
    if num == '0':
        break

    if num == reverse_num:
        print("yes")
    else:
        print("no")