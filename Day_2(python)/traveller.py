indCurr = int(input("Enter the amount required in rupees "))
curr = input("Enter the currency to convert ")
if (curr=="euro"):
    print("Euro required - " ,indCurr*0.01417)
elif (curr=="British Pound"):
    print("British Pound required - " ,indCurr*0.0100)
elif (curr=="Australian dollar"):
    print("Australian dollar required - " ,indCurr*0.02140)
elif (curr=="Canadian Dollar"):
    print("Canadian Dollar required - " ,indCurr*0.02027)
else:
    print("Invalid")
    
