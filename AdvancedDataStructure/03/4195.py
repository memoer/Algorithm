# 친구 네트워크 - 중 - 해시, 집합, 그래프 ( 제목 - 난이도 - 유형 )
# https://www.acmicpc.net/problem/4195
test_case = int(input())


def find_parent(a):
    if parent[a] == a:
        return a
    else:
        p = find_parent(parent[a])
        parent[a] = p
        return p


def union(a, b):
    parent_a = find_parent(a)
    parent_b = find_parent(b)
    if parent_a != parent_b:
        parent[parent_b] = parent_a
        number[parent_a] += number[parent_b]


for _ in range(test_case):
    f = int(input())
    parent = dict()
    number = dict()
    for _ in range(f):
        a, b = input().split(" ")
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1
        union(a, b)
        print(number[find_parent(a)])
