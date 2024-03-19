# n=int(input("Emter a number:"))
# k=0
# if(n==0 & n==1):
#     print(n,"is not prime")
# else:
#     i=2
#     while(i<n):
#         if(n%i==0):
#             k+=1
#         i+=1
# if(k==0):
#     print(n,"is a prime")
# else:
#     print(n,"is not prime")

n=int(input("enter a number:"))
k=0
if(n==0 or n==1):
    print(n,"is not prime")
else:
    i=2
    while(i<n):
        if(n%i==0):
           k=k+1
        i+=1
    if(k==0):
        print(n,"is prime")
    else:
        print(n,"is not prime")


