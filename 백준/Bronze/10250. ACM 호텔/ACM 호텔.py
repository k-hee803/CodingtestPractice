n = int(input())

for _ in range(n):
    H, W, N = map(int, input().split())
    cnt = 1

    while N > H:
        N -= H
        cnt += 1

    if cnt < 10:
        print(N, 0, cnt, sep='')
    else:
        print(N, cnt, sep='')