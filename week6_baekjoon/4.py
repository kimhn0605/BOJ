import sys  # sys.stdin.readline() 사용하기 위해선 sys import

# 빠른 입출력
t = int(sys.stdin.readline())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)