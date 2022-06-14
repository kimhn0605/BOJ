# 2061 : 좋은 암호

k, l = map(int, input().split())      # k, l 입력받기
count = 0                   # count : k 의 가장 작은 인수 

while (l > 2) :             # l 이 2보다 클 동안 반복 
  l -= 1                    # l 하나씩 줄여가면서 k의 가장 작은 인수 찾기
  if k % l == 0 :           # l 이 k 의 인수라면
    count = l               # count 갱신
    
if count == 0 :             # count 가 0이라면 GOOD 출력
  print("GOOD")
else :                      # count 가 0이 아니라면 while 문에서 갱신된거니까 BAD 출력
  print("BAD", count)