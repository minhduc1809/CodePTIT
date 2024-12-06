import math
from datetime import datetime
danhsach=[]
def sort(danhsach):
    return (-danhsach[3])
for _ in range (int(input())):
    n=input()
    dv=input()
    trich=[]
    for i in dv.split():
        trich.append(i)
    ten=''
    for i in n.split():
        trich.append(i)
    for i in trich:
        ten+=str(i[0])
    start='6:00'
    end=input()
    start_vt=datetime.strptime(start,"%H:%M")
    end_vt=datetime.strptime(end,"%H:%M")
    vttb=(120/((end_vt-start_vt).total_seconds()/3600))
    danhsach.append((ten,n,dv,vttb))
danhsach.sort(key=sort)
for i in danhsach:
    print(f'{i[0]} {i[1]} {i[2]} {i[3]:.0f} Km/h')
