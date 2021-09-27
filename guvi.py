a=2.0
print(a,"is of type",type(a))
#
p="Bhagya"
q="Sri"
r="Valle is good"
print("Valle" in r)
#
p="Bhagya"
q="Sri"
r="Valle is good"
print(p.upper())
print(p.lower())
print(p.capitalize())
#
p="Bhagya"
q="Sri"
r="Valle is good"
print(r.split())
print(r.strip())
#
p="Bhagya {}"
q="Sri"
r="Valle is good"
s=22
print(p.format(s))

#DAY 2
a=[5,10,15,20,25,30,35,40]
print(a[2])
print(a[0:3])
print(a[5:])
#changing number in list
a=[1,2,3]
a[2]=4
print(a)
#spliting string into list
a=input()
print(a.split())
#insertion
list2=[1,3,4,5]
list2.insert(1,2)
print(list2)
#extension
list2=[1,3,4,5]
list2.insert(1,2)
list2.extend([6,7,8,9])
print(list2.count())
print(list2)
#break
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1
#continue
i=1
while i<6:
    print(i)
    if i==3:
        continue
    i+=1

