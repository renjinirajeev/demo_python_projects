
# rows = 5
# k = 2 * rows - 2
for i in range(5, -1, -1):
    for j in range(5-i, 0, -1):
        print(end=" ")
    # k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")




for i in range(5, -1, -1):
    for j in range(5-i, 0, -1):
        print(end=" ")
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")



