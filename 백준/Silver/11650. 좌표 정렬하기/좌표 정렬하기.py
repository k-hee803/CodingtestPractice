import sys

N = int(sys.stdin.readline())
dots = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dots.sort()
for i in range(N):
    print(*dots[i])