#min and max numbers
"""def min_max(n,data):
    for i in range (n):
        data.append(n)
        ma=data[0]
        mi=data[0]
    for i in range (n):
        if data[i]>ma:
            ma=data[i]
        if data[i]<mi:
            mi=data[i]
    return ma,mi

n=int(input())
data=list(map(int,input().split()))
mi,ma=min_max(n,data)
print (mi,ma)"""

#min value,positions,no of times
def findmin(n,data):
    s=data[0]
    c=0
    a=[]
    for i in range (n):
        if s>data[i]:
            s=data[i]
    for i in range (n):
        if data[i]==s:
            c=c+1
            a.append(i)
    return s,c,a

n=int(input())
data=list(map(int,input().split()))
minval=findmin(n,data)
print(*minval)
