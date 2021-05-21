#recursion method
"""def mul(a,b):
    if a==1:
        return b
    if a%2:
        return b+mul(a//2,b*2)
    else:
        return 0+mul(a//2,b*2)
a,b=map(int,input().split())
print(mul(a,b))"""
#
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
       
