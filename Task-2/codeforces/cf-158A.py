#gets the first input
a=input()
#stores the values of n&k
n=int(a[0])
k=int(a[2])

#gets the second input
b=input()
#gets the k-th no
if k%2==0:
    z=((k-1)*2)
else:
    z=(2*k)-1

x=int(b[z])

if (x==0):
    print(x)

else:
#checks the next nos after k
    i=z+2
    y=len(b)
    while(i<y):
        if(int(b[i])==x):
            k=k+1
            i=i+2
        else:
            break
   #prints k
    print(k)

