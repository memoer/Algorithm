# 01. 기본 자료구조 - 01. 기초 문제풀이 (음계)
# https://www.acmicpc.net/problem/2920
a = list(map(int, input().split(" ")))

ascending = True
descending = True

for i in range(1, 8):
    if a[i - 1] < a[i]:
        descending = False
    elif a[i - 1] > a[i]:
        ascending = False

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")
