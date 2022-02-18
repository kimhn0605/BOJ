# 10818 : 최소, 최대

import sys
input = sys.stdin.readline 
n = int(input())
arr = sorted(list(map(int,input().split())))
print(arr[0], arr[len(arr)-1], end='')
