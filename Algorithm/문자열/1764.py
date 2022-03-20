# 1764 : 듣보잡

n, m = map(int, input().split())       # n, m 입력받기

# set 자료형으로 명단 입력받기 -> set() 의 교집합을 이용하기 위해
n_li = set()                          
m_li = set()

for _ in range(n) :
  n_li.add(input())
  
for _ in range(m) :
  m_li.add(input())
 
result = list((n_li & m_li))   # set() 의 교집합 & 사용해서 중복되는 이름만 저장
result.sort()                  # set() 에는 sort() 를 적용할 수 없기 때문에 리스트로 변환 후 정렬

print(len(result))

for i in result :
  print(i)