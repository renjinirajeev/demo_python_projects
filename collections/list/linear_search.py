lst=[1,9,2,6,4,3,7,10,5,8]
num=55
flag=0
for i in lst:
    if(i==num):
        flag=1
if (flag==1):
    print("element found")
else:
    print("element not found")