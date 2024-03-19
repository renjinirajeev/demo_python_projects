# str=input("enter a string:")
# rev=""
# count=len(str)
# while(count>0):
#     rev=rev+str[count-1]    #str[count-1]  --->  string in count-1 ie; length-1
#     count-=1
# print(rev)



#  USING FOR LOOP

str=input("enter a string:")
rev=""
count=len(str)
for i in range (count,0,-1):
    rev=rev+str[i-1]               #str[count-1]  --->  string in count-1 ie; length-1
print(rev)


# str = "JavaTpoint" #  string variable
# print ("The original string  is : ",str)
# reverse_String = ""  # Empty String
# count = len(str) # Find length of a string and save in count variable
# while count > 0:
#     reverse_String += str[ count - 1 ] # save the value of str[count-1] in reverseString
#     count = count - 1 # decrement index
# print ("The reversed string using a while loop is : ",reverse_String)# reversed string