import itertools
def Tinh(b):
    try:
        return eval(b)
    except:
        return None
def solve(a, dich):
    dau = ['+', '-', '*']
    ress = []
    for ops in itertools.product(dau, repeat=len(a) - 1):
        res = ""
        for i in range(len(a)):
            if a[i] < 0:
                res += f"({a[i]})"
            else:
                res += str(a[i])
            if i < len(ops):
                res += ops[i]
        if Tinh(res) == dich:
            ress.append(res)
    return ress
n, m = map(int, input().split())
a = list(map(int, input().split()))
result = solve(a, m)
if result:
    for expr in result:
        print(f"{expr}={m}")
else:
    print("IMPOSSIBLE")