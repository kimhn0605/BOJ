# 1920 : 수 찾기

n = int(input())        # n 개수만큼 숫자 입력받기
n_arr = (list(map(int, input().split())))

m = int(input())        # m 개수만큼 숫자 입력받기
m_arr = (list(map(int, input().split())))

for i in m_arr :        # m 원소 하나씩 돌면서 n_arr 배열 안에 있는지 확인
  print(1 if i in n_arr else 0)