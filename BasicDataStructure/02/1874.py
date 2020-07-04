# 02. 기본 자료구조 - 02. 핵심 유형 문제풀이 (스택 수열)
# https://www.acmicpc.net/problem/1874
n = int(input())
stack = []
result = []
count = 1

for _ in range(n):
    data = int(input())
    while count <= data:
        stack.append(count)
        result.append("+")
        count += 1
    if stack[-1] == data:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit(0)

print("\n".join(result))
