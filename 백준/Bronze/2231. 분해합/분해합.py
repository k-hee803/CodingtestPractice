N = int(input())
result = 0
for i in range(1, N):
    num = list(map(int, str(i)))
    M = i + sum(num)
    if M == N:
        result = i
        break
print(result)