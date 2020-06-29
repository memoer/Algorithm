# 01. 기본 자료구조 - 01. 기초 문제풀이 (블랙잭)
# https://www.acmicpc.net/problem/2798
n, m = list(map(int, input().split(" ")))
data = list(map(int, input().split(" ")))

result = 0

for i in range(len(data)):
    for j in range(i + 1, len(data)):
        for k in range(j + 1, len(data)):
            temp = data[i] + data[j] + data[k]
            if temp <= m:
                result = max(temp, result)

print(result)
