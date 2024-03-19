num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))

if(num1<num2<num3):
    print("Lowest number is",num1)
elif(num1>num2<num3):
    print("Lowest number is", num2)
else:
    print("Lowest number is", num3)