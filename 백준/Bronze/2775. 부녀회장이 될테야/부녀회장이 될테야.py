from re import L

N = int(input())
for _ in range(N):
    k = int(input())
    n = int(input())

    num = [i for i in range(1,15)]

    for i in range(k):
        for j in range(1, n):
            num[j] += num[j-1] 

    print(num[n-1])