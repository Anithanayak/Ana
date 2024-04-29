def lsearch(x):
    flag=0
l=[20,40,25,60,80,85]
item=int(input("enter an item"))
for i in range (0,len(l)):
    if (l[i]==item):
        f=1
        loc=i
    break
if(f==1): 
   print("search successfull %d is present at %d"%(item))
else:
   print("not successfull") 
