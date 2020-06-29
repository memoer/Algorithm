# 키로거 - 중 - 스택, 구현, 그리디 ( 제목 - 난이도 - 유형 )
# https://www.acmicpc.net/problem/5397
test_case = int(input())

for _ in range(test_case):
    data = input()
    left_stack = []
    right_stack = []
    for i in data:
        if i == "-":
            if left_stack:
                left_stack.pop()
        elif i == "<":
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == ">":
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)
    left_stack.extend(reversed(right_stack))
    print("".join(left_stack))
