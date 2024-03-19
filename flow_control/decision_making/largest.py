# Take input of age of 3 people by user and determine
# oldest and youngest among them.


age1=int(input("Enter age 1:"))
age2=int(input("Enter age 2:"))
age3=int(input("Enter age 3:"))

if(age1>age2>age3):
    print("Age 1 is largest",age1)
    print("Age 3 is smallest ",age3)
elif(age1<age2>age3)&(age1<age3):
    print("Age 2 is largest", age2)
    print("Age 1 is smallest ", age1)
elif(age1<age2>age3)&(age3<age1):
    print("Age 2 is largest", age2)
    print("Age 3 is smallest ", age3)
elif(age1<age2<age3):
    print("Age 3 is largest", age3)
    print("Age 1 is smallest", age1)
else:
    print("Please Input the correct age")