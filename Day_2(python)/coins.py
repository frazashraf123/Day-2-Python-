rs1 = int(input())
rs5 = int(input())
aval = int(input())
if(rs1*1 + rs5*5 >= aval):
    if(aval//5 > rs5 ):
        five = rs5
    else:    
        five = aval//5
   
    aval = aval - (five*5)
    if(aval>rs1):
        print("-1")
    else:    
        print(five , "five" , aval , "one") 
else:
    print("-1")
