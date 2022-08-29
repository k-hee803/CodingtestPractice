N = int(input())
seats = input()
holder = 0
num = ['S', 'LL']
for i in range(2):
    holder += seats.count(num[i])
if N <= holder:
    print(N)
else:
    print(holder + 1)