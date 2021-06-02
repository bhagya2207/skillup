#primenumbers count
"""import math as m
def isprime(num):
    s=int(m.sqrt(num))
    for i in range(2,s+1):
        if n%i==0:
            return 0
    return 1
def countPrimes(n,data):
    pc=0
    for i in data:
        if isprime(i):
            pc+=1
    return pc
   
n=int(input())
data=list(map(int,input().split()))
pc=countPrimes(n,data)
print(pc)"""

#print primes
"""import math as m
def isprime(num):
    s=int(m.sqrt(num))
    for i in range(2,s+1):
        if num%i==0:
            return 0
    return 1
def findPrimes(n,data):
    c=[]
    for i in data:
        if isprime(i):
            c.append(i)
    return c
    
n=int(input())
data=list(map(int,input().split()))
primes=findPrimes(n,data)
print(*primes)"""
#primes & non primes
"""import math as m
def isprime(num):
    if num==1:
        return 0
    s=int(m.sqrt(num))
    for i in range(2,s+1):
        if num%i==0:
            return 0
    return 1
def findPrimes(n,data):
    prime=[]
    nonprimes=[]
    for i in data:
        if isprime(i):
            prime.append(i)
        else:
            nonprimes.append(i)
    return prime,nonprimes
    
    
n=int(input())
data=list(map(int,input().split()))
primes,np=findPrimes(n,data)
print(primes)
print(np)"""
#sum of primes and non primes
"""import math as m
def isprime(num):
    if num==1:
        return 0
    s=int(m.sqrt(num))
    for i in range(2,s+1):
        if num%i==0:
            return 0
    return 1
def findPrimes(n,data):
    prime=[]
    nonprimes=[]
    for i in data:
        if isprime(i):
            prime.append(i)
        else:
            nonprimes.append(i)
    return sum(prime),sum(nonprimes)
  
n=int(input())
data=list(map(int,input().split()))
primes,np=findPrimes(n,data)
print(primes)
print(np)"""
#sum of digits
"""import math as m
def isprime(num):
    if num==1:
        return 0
    s=int(m.sqrt(num))
    for i in range(2,s+1):
        if num%i==0:
            return 0
    return 1
def sumofdigits(n,data):
    p=[]
    np=[]
    for i in data:
        if isprime(i):
            p.append(i)
            l=sum(p)
        else:
            np.append(i)
            k=sum(np)
    return l,k     
       
n=int(input())
data=list(map(int,input().split()))
prime=sumofdigits(n,data)
print(*prime)"""
#reverse
"""def revofdigits(data,n):
    for i in range(n):
        rev=0
        while data[i]:
            r=data[i]%10
            data[i]=data[i]//10
            rev=rev*10+r
        data[i]=rev
n=int(input())
data=list(map(int,input().split()))
rev=revofdigits(data,n)
print(*data)"""
#palindrome
def pali(n):
    temp=n
    sum=0
    while n>=0:
        r=n%10
        n=n//10
        sum=sum*10+r
    return sum==temp
def palindrome(n,data):
    c=0
    for i in range(len(data)):
        if pali(data[i]):
            c=c+1
    return c
n=int(input())
data=list(map(int,input().split()))
print(palindrome(n,data))



