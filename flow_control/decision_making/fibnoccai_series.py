a,b=0,1
n=10
lst=[]
for i in range(1,n):
    # print(a)
    lst.append(a)
    a,b=b,a+b
print(lst)
lst.sort(reverse=True)
for i in lst:
    print(i)


# Python 3 Program to print Fibonacci
# series in reverse order

# def reverseFibonacci(n):
#     a = [0] * n
#
#     # assigning first and second elements
#     a[0] = 0
#     a[1] = 1
#
#     for i in range(2, n):
#         # storing sum in the
#         # preceding location
#         a[i] = a[i - 2] + a[i - 1]
#
#     for i in range(n - 1, -1, -1):
#         # printing array in
#         # reverse order
#         print(a[i], end=" ")
#
#     # Driver function
#
#
# n = 20
# reverseFibonacci(n)

# a=[0,1]
# n=20
# for i in range(2,n):
#     a[i] = a[i - 2] + a[i - 1]
# for i in range(n-1,-1,-1):
#     print(a[i],end=' ')



