#input the no of entries
n=int(input())

#input the entries as a list
s=input()
list=s.split()
#gets the ist value
m=list[1]

i=1
cnt=0
#checks for the the max. no.
while i<n:
    if int(list[i])>=int(m) :
        m=list[i]
        cnt=cnt+1
    i=i+1
#prints the count of max. no.    
print(cnt+1) if cnt==0 else print(cnt)
