#LCM of number
def lcm(a,b):
    t=2
    res=1
    while True:
        if a%t==0 and b%t==0:
            a=a//t
            b=b//t
            res=res*t
        else:
            t+=1
        if a<t or b<t:
            return res*a*b   
a,b=map(int,input().split())
print(lcm(a,b))

#LCM using recursion
def lcm(a,b,t):
    if a<t or b<t:
        return a*b
    if a%t==0 and b%t==0:
        return t*lcm(a//t,b//t,t)
    else:
        return lcm(a,b,t+1)
    
a,b=map(int,input().split())
print(lcm(a,b,2))

#LCM with maximum number method
def lcm(a,b):
    m=max(a,b)
    while True:
        if m%b==0 and m%a==0:
            return m
        else:
            m+=1
a,b=map(int,input().split())
print(lcm(a,b))

#GCD of numbers
def gcd(a,b):
    while True:
        if a>b:
            a,b=b,a
        b=b%a
        if b==0:
            return a
  
a,b=map(int,input().split())
print(gcd(a,b))

#factors of number
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i)
        
#count of factors of numbers
from math import*
n=int(input())
s=int(sqrt(n))
t=2
for i in range(2,s+1):
    if n%i==0:
        if i==n/i:
            t=t+1
        else:
            t=t+2
print(t)














