# 02. 기본 자료구조 - 02. 핵심 유형 문제풀이 (프린터 큐)
# https://www.acmicpc.net/problem/1966
test_case = int(input())

for _ in range(test_case):
    n, m = list(map(int, input().split(" ")))
    papers = list(map(int, input().split(" ")))
    papers = [(priority, index) for (index, priority) in enumerate(papers)]
    count = 0
    while True:
        if papers[0][0] == max(papers, key=lambda x: x[0])[0]:
            count += 1
            if papers[0][1] == m:
                print(count)
                break
            else:
                papers.pop(0)
        else:
            papers.append(papers.pop(0))
