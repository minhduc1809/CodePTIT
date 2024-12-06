u = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
t = int(input())
for i in range(t):
    n, k = [int(_) for _ in input().split()]
    s = ''
    while n > 0:
        x = n % k
        s = u[x] + s
        n = int(n / k)
    print(s)