week=int(input("enter number:"))
if(0<week<=7):
    if(week==1):
        print("sunday")
    elif(week==2):
        print("monday")
    elif (week == 3):
        print("tueday")
    elif (week == 4):
        print("wednesday")
    elif(week==5):
        print("thrusday")
    elif (week == 6):
        print("friday")
    else:
        print("saturday")
else:
    print("enter valid number")
