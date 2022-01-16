#알파벳 찾기
import sys
N = sys.stdin.readline()

list_result = list(range(97,123))

for i in list_result:
    print(N.find(chr(i)))