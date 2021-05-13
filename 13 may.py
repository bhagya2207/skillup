#replace with multiples of given number
n,sv,rv=map(int,input().split())
nn=0
temp=n
c=0
if rv>10:
    rv=rv%10+1
while n:
    r=n%10
    n=n//10
    c+=1
n=temp
c=c-1
while c!=-1 or n!=0:
    
    r=n//pow(10,c)
    n=n%pow(10,c)
    c-=1
    if r%sv==0:
        r=rv
        rv+=1
        if rv==10:
            rv=1
    nn=nn*10+r
print(nn)
