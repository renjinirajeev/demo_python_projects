lst=[12,34,50,67,81]
lst1=[]
sum = 0
for i in lst:

    for j in str(i):
        sum+=int(j)
    lst1.append(sum)
print(str(lst1))

#

# Python3 code to demonstrate
# Sum of number digits in List
# using loop + str()

# # Initializing list
# test_list = [12, 67, 98, 34]
#
# # printing original list
# print("The original list is : " + str(test_list))
#
# # Sum of number digits in List
# # using loop + str()
# res = []
# for ele in test_list:
#     sum = 0
#     for digit in str(ele):
#         sum += int(digit)
#     res.append(sum)
#
# # printing result
# print("List Integer Summation : " + str(res))

