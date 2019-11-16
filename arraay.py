from array import *
val=array('l',[])
n=int(input('enter a lenth of no:'))
for i in range(n):
    x=int(input('enter the no:'))
    val.append(x)


print(val)

ent=eval(input('enter you want:'))

k=0
for e in val:
    if e==ent:
        print(k)
        break
    k+=1
if e!=ent:

    print("this number is't there ")



