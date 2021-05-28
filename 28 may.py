#pattern1
"""n=int(input("Enter number: "))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()"""
#pattern 2
"""n=int(input("Enter number: "))
for i in range(n):
    for j in range(n):
        print(j+1,end=" ")
    print()"""
#pattern 3
"""n=int(input("Enter number: "))
for i in range(n,0,-1):
    for j in range(n,0,-1):
        print(j,end=" ")
    print()"""
#pattern 4
"""n=int(input("Enter number: "))
for i in range(n):
    if i%2==0:
        for j in range(1,n+1):
            print(j,end=" ")
    else:
        for j in range(n,0,-1):
            print(j,end=" ")
    print()"""
#pattern 5
"""n=int(input("Enter number: "))
for i in range(n):
    if i%2==0:
        for j in range(1,n+1):
            print(j,end=" ")
    else:
        for j in range(1,n+1):
            print(i,end=" ")
    print()"""
#pattern 6
"""n=int(input("Enter number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1:
            print(i,end=" ")
        else:
             print(i,end=" ")
    print()"""
#pattern 7
"""n=int(input("Enter number: "))
for i in range(n):
    if i%2==0:
        for j in range(1,n+1):
            print(j,end=" ")
    else:
        for j in range(n,0,-1):
            print(i,end=" ")
    print()"""
#pattern 8
"""n=int(input("Enter number: "))
for i in range(1,n+1):
    for j in range(n,0,-1):
        if i%2==1:
            print(j,end=" ")
        else:
            print(i,end=" ")
    print()"""
#pattern 9
"""n=int(input("Enter number: "))
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j%2==0:
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()"""
#pattern 10
n=int(input("Enter number: "))
for i in range(1,n+1):
    if i%2!=0:
        for j in range(n,0,-1):
            if j%2==0:
                print(0,end=" ")
            else:
                print(1,end=" ")
        print()
    else:
        for j in range(n,0,-1):
            if j%2==0:
                print(1,end=" ")
            else:
                print(0,end=" ")
        print()

        



            











