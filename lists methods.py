#data is in different lines
n=int(input())
data=[None for i in range(n)]
for i in range(n):
    val=int(input())
    data[i]=val
print(data)

#simple method
n=int(input())
data=list(map(int,input().split()))
print(data)

#index based
n=int(input())
data=list(map(int,input().split()))
for i in range(n):
    print(i,data[i])
    
#value based
n=int(input())
data=list(map(int,input().split()))
for i in data:
    print(i,end=" ")
    
#sum of list of elements
n=int(input())
data=list(map(int,input().split()))
res=0
for i in range(n):
    res=res+data[i]
print(res)

#sum using functions
def total_marks(n,data):
    res=0
    for i in data:
        res+=i
    return res
n=int(input())
data=list(map(int,input().split()))
total=total_marks(n,data)
print (total)

#number of even and odd
def even_odd(n,data):
    ec=0
    oc=0
    for i in data:
        if i%2==0:
            ec+=1
        else:
            oc+=1
    return (ec,oc)
n=int(input())
data=list(map(int,input().split()))
total=even_odd(n,data)
print (total)
