# Python program to interchange first and last elements in a list
# lst=[1,2,4,6,2,7,3,8,0,2,9]
# i=len(lst)
# lst[0],lst[i-1]=lst[i-1],lst[0]
# print(lst)


# Python3 program to swap elements
# at given positions

# Swap function
# def swapPositions(list, pos1, pos2):
#     list[pos1], list[pos2] = list[pos2], list[pos1]
#     return list
#
#
# # Driver function
# List = [23, 65, 19, 90]
# pos1, pos2 = 1, 3
#
# print(swapPositions(List, pos1 , pos2 ))


# swap string in list
# lst=['hai','bie','hello','goodbye']
# i=len(lst)
# lst[0],lst[2]=lst[2],lst[0]
# print(lst)


# max of two numbers in python
#
# lst=[22,65,21,67,34,11,9,48,37]
# i=min(lst)
# print(i)
# lst.remove(i)
# j=min(lst)
# print(j)
# lst.remove(j)
# lst.append(i)
# lst.append(j)
# print(lst)


# Python | Ways to check if element exists in list


# lst=[22,45,2,6,3,33,22,65,21,67,34,11,9,48,37]
# flag=0
# num=int(input('enter a number:'))
# for i in lst:
#     if(num==i):
#         flag=1
# if(flag==1):
#     print('element found')
# else:
#     print('element not found')



# reverse a list
# lst = [22, 45, 2, 6, 3, 33, 22, 65, 21, 67, 34, 11, 9, 48, 37]
# lst1=lst[::-1]
# print(lst1)


# # Python | Count occurrences of an element in a list
# lst = [22, 45, 2, 6, 3, 33, 22, 65, 21, 67, 34, 11, 9,3,48, 3]
# num=int(input('number:'))
# count=0
# for i in lst:
#     if(num==i):
#         count+=1
# print(num,'occurs in',count)


# digits sum in a list
# #
# lst = [22, 45, 2, 6, 3, 33, 22, 65, 21, 67, 34, 11, 9, 48, 37]
# lst1=[]
# for i in lst:
#     sum = 0
#     for j in str(i):
#         sum += int(j)
#     lst1.append(sum)
# print(str(lst1))
#
#
# lst = [22, 45, 2, 6, 3, 33, 22, 65, 21, 67, 34, 11, 9, 48, 37]
# lst1 = []
# for i in lst:
#     sum = 0
#     for j in str(i):
#         sum += int(j)
#     lst1.append(sum)
# print(str(lst1))

lst = [22, 45, 2, 6, 3, 33, 22, 65, 21, 67, 34, 11, 9, 48, 37]
lst1=[]
for i in lst:
    sum=0
    for j in str(i):
        sum+=int(j)
    lst1.append(sum)
print(str(lst1))

