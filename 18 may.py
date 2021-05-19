#multiplication sum
a,b=map(int,input().split())
sum=0
while True:
    if a%2:
        sum=sum+b
    a=a//2
    b=b*2
    if a==0:
        break      
print(sum)

# above program using functions
def mul(a,b):
    sum=0
while True:
    if a%2:
        sum=sum+b
    a=a//2
    b=b*2     
print(sum)
a,b=map(int,input().split())

#number series
n=int(input())
while True:
    if n%2==0:
        n=n//2
        print(n,end=" ")
    else:
        n=3*n+1
        print(n,end=" ")
    if n==1:
        break

    
    
    
