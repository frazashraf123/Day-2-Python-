adults = int(input())
child = int(input())
adultcost = adults*37550 
childcost = ((1/3)*37550)*child
totalcostadult = (7/100)*adultcost + adultcost
totalcostchild = (7/100)*childcost + childcost
discountadult = totalcostadult - ((10/100)*totalcostadult)
discountchild = totalcostchild - ((10/100)*totalcostchild)
totalcost = discountadult+discountchild
print(totalcost)
print((((((adults*37550.0)+(child*37550.0*0.3)

