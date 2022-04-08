# 2163 : 초콜릿 자르기

n, m = map(int, input().split())    # n, m 입력받기

print(n*m-1)   # 초콜릿 나누는 횟수 : (n-1) + ((m-1) * n)