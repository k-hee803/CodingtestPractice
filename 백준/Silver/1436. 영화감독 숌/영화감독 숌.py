N = int(input())
count = 0

for i in range(N*1000):
    if str(i).find("666") != -1:
        count += 1
        if count == N:
            print(i)