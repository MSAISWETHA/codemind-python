N=int(input())
square=N**2
sum=0
while(square!=0):
    rem=square%10
    sum=sum+rem
    square=square//10
if (sum==N):
    print("Neon Number")
else:
    print("Not Neon Number")
    
    