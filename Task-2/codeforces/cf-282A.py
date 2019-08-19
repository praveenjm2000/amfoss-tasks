#takes the input of n
n=int(input())
x=0
#executes the loop n times
while n>0:
    s=input()
    #increments x
    if (s=='++X' or s=='X++'):
        x=x+1
    #decriments x
    elif (s=='--X' or s=='X--'):
        x=x-1
    n=n-1
print(x)
    
