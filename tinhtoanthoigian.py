from datetime import datetime
danhsach=[]
for _ in range(int(input())):
    id=input().strip()
    n=input().strip()
    start_time=datetime.strptime(input().strip(),"%H:%M")
    end_time=datetime.strptime(input().strip(),"%H:%M")
    time_h = end_time - start_time
    total_minutes = time_h.total_seconds() / 60
    hours = int(total_minutes // 60)
    minutes = int(total_minutes % 60)

    danhsach.append((id, n, hours, minutes))

danhsach.sort(key=lambda x: (x[2] * 60 + x[3]), reverse=True)

for i in danhsach:
    print(f"{i[0]} {i[1]} {i[2]} gio {i[3]} phut")