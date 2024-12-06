s=input().split()
if int(s[0])<=0 or int(s[1])<=0:
    print("INVALID")
else:
    print(f"{(int(s[0])+int(s[1]))*2} {(int(s[0])*int(s[1]))} {s[2][0].upper()+s[2][1::].lower()}")