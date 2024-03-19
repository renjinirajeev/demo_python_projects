n=int(input('enter a number:'))
a,b=0,1
for i in range(1,n+1):
    print(a)
    a,b=b,a+b
# #     if(a%2==0):
# #         print(a)
#
# limit = 100
# sum = 0
# a = 1
# b = 1
# while b < limit:
#
#     if b % 2 == 0: sum += b
#     h = a + b
#     a, b = b, h
#
# print(sum)
