#super min
"""def reverse(n):
    rev=0
    while n:
        r=n%10
        n=n//10
        rev=rev*10+r
    return rev
def findmin(n,data):
    s=min(data)
    r=reverse(s)
    for i in range(n):
        if data[i]==s:
            data[i]=r
    s=min(data)
    print(s)
    print(data)
    return s==r

n=int(input())
data=list(map(int,input().split()))
minval=findmin(n,data)
print(minval)"""
#super max
"""def reverse(n):
    rev=0
    while n:
        r=n%10
        n=n//10
        rev=rev*10+r
    return rev
def findmin(n,data):
    s=max(data)
    r=reverse(s)
    for i in range(n):
        if data[i]==s:
            data[i]=r
    s=max(data)
    print(s)
    print(data)
    return s==r

n=int(input())
data=list(map(int,input().split()))
minval=findmin(n,data)
print(minval)"""
#original number
"""def org(n,data):
    t=[]
    for i in data:
        if i not in t:
            t.append(i)
    return t

n=int(input())
data=list(map(int,input().split()))
d=org(n,data)
print(*d)"""
#
def findmin(n,data):
    d=[]
    for i in data:
        if i not in d:
            d.append(i)
    return d
n=int(input())
data=list(map(int,input().split()))
minval=findmin(n,data)
print(*data)







