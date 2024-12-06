pre, res, _ = -1, [], input()
try:
    while True:
        l = len(input().split())
        if l == 6: 
            input()
            if l != pre: res.append(1)
        else: 
            res.append(2)
            for i in range(3): input()
        pre = l
except: pass
print(len(res))
for i in res: print(i)