N = int(input())
people = [list(input().split()) for _ in range(N)]

people.sort(key=lambda x:int(x[0]))
for i in range(N):
    print(*people[i])