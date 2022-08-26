N = int(input())
numbers = list(map(int, input().split()))

count = 0
for i in range(N):
    cnt = 0
    if numbers[i] < 2 :
        pass
    elif numbers[i] == 2:
        count += 1
    else:
        for j in range(2, numbers[i]):
            if numbers[i] % j == 0:
                cnt += 1
        if cnt == 0:
            count += 1
print(count)