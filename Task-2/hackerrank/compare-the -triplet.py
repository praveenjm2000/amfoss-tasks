#gets the input
x=input()
y=input()
#stores as list
a=x.split()
b=y.split()

i=0
c1=0
c2=0
#compares each no of a and b
while (i<3):
    if int(a[i])>int(b[i]):
        c1=c1+1
    elif int(a[i])<int(b[i]):
        c2=c2+1
    i=i+1

print(c1,c2)
