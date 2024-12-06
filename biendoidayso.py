import math
def count(a):
    if a[0] == a[1] and a[1] == a[2] and a[2] == a[3]:
        return 0
    e = []
    for i in range(4):
        e.append(abs(a[i] - a[(i+1)%4]))
    return count(e) + 1
while True:
    a = [int(x) for x in input().split()]
    if a == [0, 0, 0, 0]: break
    print(count(a))