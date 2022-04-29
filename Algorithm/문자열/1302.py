# 1302 : 베스트셀러

n = int(input())                # n 입력받기
li = dict()                     # 딕셔너리형 선언
result = []               

for _ in range(n) :
  book = input()                # 책 이름 입력받기
  
  if book in li.keys() :        # 책이 li 에 이미 있다면
    li[book] += 1               # 권수 += 1
  else :                        # 책이 li 에 없다면
    li[book] = 1                # 1권으로 새롭게 추가
    
max_num = max(li.values())                # max_num : 가장 많이 팔린 권수 

li = sorted(li.items(), reverse=True)     # 많이 팔린 권수대로 내림차순으로 정렬 
# li.items().sort(reverse=True) -> 오류

# 가장 많이 팔린 책이 여러 개일때 사전 순으로 정렬
for i in li :                 # 이차원 리스트를 하나씩 순회하면서
  if i[1] == max_num :        # 권수가 max_num 과 같다면
    result.append(i[0])       # result 에 책 제목 저장
    
result.sort()       # result 오름차순 정렬 -> 알파벳 순서대로 정렬
print(result[0])    # 가장 앞서는 제목 출력