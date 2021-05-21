#recursion method
def mul(a,b):
    if a==1:
        return b
    if a%2:
        return b+mul(a//2,b*2)
    else:
        return 0+mul(a//2,b*2)
a,b=map(int,input().split())
print(mul(a,b))
#recursion in fib
def fib(a,b,d,n):
    if d>n:
        return
    if d==1:
        print(a,end=" ")
        d+=1
    if d==2:
        print(b,end=" ")
        d+=1
    print(a+b,end=" ")
    fib(b,a+b,d+1,n)
n=int(input())
fib(0,1,1,n)

#armstrong number
def arm(num):
    n=num
    s=0
    while n>0:
        r=n%10
        s+=(r*r*r)
        n=n//10
    if n==s:
        print("armstrong")
    else:
        print("armstrong")

num=int(input("enter a number"))
arm(num)

#perfect number
def per(num):
    n=num
    s=0
    i=1
    while i<n:
        if n%i==0:
            s=s+i
        i=i+1
    if n==s:
        print("perfect number")
    else:
        print("not a perfect number")

num=int(input("enter a number"))
per(num)
       
