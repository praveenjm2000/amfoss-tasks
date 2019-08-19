#gets the input 
s=input()
#gets the first value
x=s[0]
n=len(s)
i=1
cnt=1
#runs the loop n-1 times
while(i<n):
    #incr 1 if next no is same
    if (s[i]==x):
        cnt=cnt+1
    #if not, changes x with prev value
    else:
        x=s[i]
    #incr i
    i=i+1
#print output
print('YES') if (cnt>=7) else print('NO')  
