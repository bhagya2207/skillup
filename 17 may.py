#fibanocci series
"""def gen_fib(n,a=0,b=1):
    if n==0:
        return
    if n==1:
        print(0)
        return
    print(a,b,end=" ")
    for i in range(3,n+1):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
n=int(input())
gen_fib(n)"""
#fibanocci series with in limits
def gen_fib(n,m,a=0,b=1):
    if n==0:
        print(a,b,end=" ")
    if n==1:
        print(b,end=" ")
    c=0
    while c<=m:
        c=a+b
        if c>=n and c<=m:
            print(c,end=" ")
        a=b
        b=c
n,m=map(int,input().split())
gen_fib(n,m)

