#pronic number
n=int(input())
f=0
for i in range(1,n):
    if n==i*(i+1):
        f=1
        break
if f==1:
    print("Pronic Number")
else:
    print("Not Pronic Number")
    
#disurium number
def dis(n):
    count=0
    a=0
    temp=n
    while n!=0:
        
        n=n//10
        count+=1
    n=temp
    while temp!=0:
        r=n%10
        n=n//10
        a=a+pow(r,count)
        count=count-1
        if a==temp:
            print("Disurium")
        else:
            print("Not Disurium")   
n=int(input())
print(dis(n))

#harshad number
n=int(input())
sum=0
temp=n
while temp>0:
    r=temp%10
    temp=temp//10
    sum=sum+r
if n%sum==0:
    print("harshad")
else:
    print("Not harshad")






    
