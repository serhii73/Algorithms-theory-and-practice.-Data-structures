import sys
sys.setrecursionlimit(30000)
N = int(input())
DATA = list(map(int, input().split()))
D = {}
for idx, i in enumerate(DATA):
    D.setdefault(i, []).append(idx)
def height(number):
    """return max h"""
    child = D.get(number, [])
    h = 1
    for son in child:
        h = max(h, height(son) + 1)
    return h

REZULT = height(-1) - 1
print(REZULT)
