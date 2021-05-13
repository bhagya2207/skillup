n=int(input("Enter Number: "))
temp=n
c=d=f=l=nn=0
while n:
    r=n%10
    n=n//10
    c=c+1
d=c=c-1
n=temp
if n>0:
    f=n//pow(10,c)
    l=n%10
while n:
    r=n%10
    n=n//10
    if c==d:
        r=f
    if c==0:
        r=l
    nn=nn*10+r
    c=c-1
print(nn)
