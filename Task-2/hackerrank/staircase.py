n=int(input())
i=1
while i<=n:
    j=n-i
    while j>0:
        print(' ',end='')
        j=j-1
    k=1
    while k<=i:
        print('#',end='')
        k=k+1
    print('')
    i=i+1
