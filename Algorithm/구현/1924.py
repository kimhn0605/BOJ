# 1924 : 2007년
 
x, y = map(int, input().split())      # x, y 입력받기
count = 0

day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
dict1 = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}

for i in range(1, x) :      # 1월부터 x 이전달까지 반복
  count += dict1[i]         # count : x월 y일까지의 총 일수
count += y                  # x 달에 포함되는 y 일수 추가

print(day[(count-1) % 7])   # 7로 나눈 나머지를 인덱스로 지정하여 요일 출력