#print max and min
n=int(input("Enter Number: "))
mi=9
ma=0
while n:
    r=n%10
    n=n//10
    if r>ma:
        ma=r
    if r<mi:
        mi=r
print(mi,ma)


#number of max and min terms
n=int(input("Enter Number: "))
mi=9
ma=0
c=d=0
while n:
    r=n%10
    n=n//10
    if r>ma:
        ma=r
    else r==ma:
        c+=1
    if r<mi:
        mi=r
    else r==mi:
        d+=1
print(mi,ma,c,d)
