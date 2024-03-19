#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5


# for i in range(1,6):
#     for j in range(6,1,-1):
#         print(j,end=" ")
#     print()

# right triangle pattern

for i in range(1,6):
    for j in range(1, 6 - i):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(k, end=' ')
    print()
