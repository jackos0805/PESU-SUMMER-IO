l=eval(input("enter a list:"))
num=float(input ('enter number to be found:'))
a=len(l)
b=len(l)
l.sort()
i=0
while True:
    mid=int(a/2)
    if l[mid]==num:
        print('num found')
        break
    elif l[mid]>num:
        a=mid
    elif l[mid]<num:
        a=len(l[(mid+1):a])
        l=l[(mid+1):len(l)]
    if i==b:
       print('no num')
       break
    i+=1
