# #create a simple calculator using function
#
#
# def cal():
#     print("1. Addition")
#     print("2. Substraction")
#     print("3. Multiplication")
#     print("4. Division")
#     i=int(input("Enter your choice:"))
#     if(i==1):
#         def add():
#            num1 = int(input("enter number1:"))
#            num2 = int(input("enter number2:"))
#            sum=num1+num2
#            return sum
#         add()
#     elif(i==2):
#         def sub():
#             num1 = int(input("enter number1:"))
#             num2 = int(input("enter number2:"))
#             dif=num1-num2
#             return dif
#         data1= sub(5, 7)
#         print(data1)
#     elif(i==3):
#         def multi(num1, num2):
#             mul=num1*num2
#             return mul
#         data2 = multi(5, 7)
#         print(data2)
#     elif(i==4):
#         def divi (num1, num2):
#             div=num1/num2
#             return div
#         data3= divi(5, 7)
#         print(data3)
#     else:
#         def msg(mes):
#             mes='invalid choice'
#             return mes
#         data4 = msg('invalid choice')
#         print(data4)
# cal(1,5)
#
#


def add(num1,num2):
    res=num1+num2
    return res

def sub(num1,num2):
    res=num1-num2
    return res
def mul(num1,num2):
    res=num1*num2
    return res
def div(num1,num2):
    res=num1/num2
    return res

print("1. Addition \n"
      "2. Substraction\n" 
      "3.Mu "
       4. Division)
