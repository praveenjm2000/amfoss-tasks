
r=int(input())      # input no of rows/column
c=r
matrix = []

# For user input 
for i in range(r):          # for loop for row entries 
    l=input()
    m=l.split()
    a=[]
    for j in range(c):      # for loop for column entries 
        a.append(int(m[j])) 
    matrix.append(a)

p=0
for i in range(r):          # for loop for findin sum of 1st diogonal
    for j in range(c):
        if int(i)==int(j):
            p=p+int(matrix[i][i])
            
q=0                         # for loop for findin sum of 2nd diogonal
j=r-1   
for i in range(c):
    q=q+int(matrix[i][j])
    j=j-1

s=p-q                # find abs sum
if s<0:
    s*=-1
print(s)

        
    
    
