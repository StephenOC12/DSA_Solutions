# python3

import sys


class Rope:
    def __init__(self, s):
        self.s = s

    def result(self):
        return self.s

    def process(self, i, j, k):
        s_list = list(self.s)
        substring = s_list[i:j + 1]
        del s_list[i:j + 1]
        s_list[k:k] = substring
        self.s = ''.join(s_list)


rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    rope.process(i, j, k)
print(rope.result())
