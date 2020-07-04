# 수 찾기 - 하 - 해시, 배열, 구현 ( 제목 - 난이도 - 유형 )
# https://www.acmicpc.net/problem/1920
n = int(input())
array = set(map(int, input().split(" ")))

m = int(input())
data = list(map(int, input().split(" ")))

for i in data:
    if i in array:
        print("1")
    else:
        print("0")
