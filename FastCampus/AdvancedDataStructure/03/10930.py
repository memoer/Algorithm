# SHA-256 - 하 - 해시, 구현 ( 제목 - 난이도 - 유형 )
# https://www.acmicpc.net/problem/10930
import hashlib

string = input()
print(hashlib.sha256(string.encode("utf-8")).hexdigest())
