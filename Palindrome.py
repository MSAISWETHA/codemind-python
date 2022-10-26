n=int(input())
rev=0
m=n
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if m==rev:
    print('True')
else:
    print(False)