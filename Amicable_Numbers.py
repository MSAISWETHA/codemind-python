n=int(input())
m=int(input())
p_n=0
for i in range(1,n):
    if n%i==0:
        p_n+=i
p_m=0
for i in range(1,m):
    if m%i==0:
        p_m+=i
if p_n==m:
    print('Amicable')
else:
    print('Not Amicable')