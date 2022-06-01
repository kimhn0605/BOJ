# 1927 : 최소 힙

import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n) :
  x = int(sys.stdin.readline())
  if x == 0 :
    if len(heap) == 0 :
      print(0)
      continue
    else :
      print(heapq.heappop(heap))
  else :
    heapq.heappush(heap, x)