lst=[1,8,3,5,2,7,9,10,4,6]
num=99
low=0
upper=len(lst)-1
flag=0
for i in lst:
    mid=(low+upper)//2
    if(num>lst[mid]):
        low=mid+1
    elif(num<lst[mid]):
        upper=mid-1
    else:
        flag=1
if(flag==1):
    print("element found")
else:
    print("element not found")

