# 15596 : 정수 N개의 합

def solve(a) :
  ans = 0
  for i in range(len(a)) :   # a가 리스트인데 그냥 a라고 넘겨주면 런타임 에러
    ans += a[i]
  return ans
