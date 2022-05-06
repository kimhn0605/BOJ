# 5635 : 생일

n = int(input())        # n 입력받기
info = dict()           # 빈 딕셔너리 선언

for i in range(n) :     # 학생 수만큼 반복
  data = input().split()        # 이름, 생일 일, 월, 연도 입력받기
  data[1:] = map(int, data[1:])  # 일, 월, 연도 숫자형으로 변환
  info[data[0]] = list(reversed(data[1:]))    # '이름 : [연도, 월, 일]' 형태로 저장

# 딕셔너리 값을 기준으로 내림차순 정렬 (늦게 태어난 순으로 정렬)
result = sorted(info.items(), reverse = True, key = lambda info:info[1])

# 가장 나이 적은 사람, 가장 나이 많은 사람 이름만 출력
print(result[0][0], result[-1][0], sep="\n")