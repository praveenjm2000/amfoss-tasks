s=input()
if s[8]=='P' :
    am=int(s[0:2])
    pm=am+12
    print(pm,s[2:8],sep='')
else :
    print(s[0:8])


