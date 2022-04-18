# 3052 : 나머지

li = set()              # set 자료형 변수 선언

for _ in range(10) :
  x = int(input())
  li.add(x % 42)        # 42로 나눈 나머지 저장 (중복값은 자동 제거)

print(len(li))          # 서로 다른 나머지 개수 출력