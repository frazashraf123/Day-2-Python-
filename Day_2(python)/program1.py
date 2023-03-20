#list
list1=[]
print(list1,type(list1))
list2=[10,20,30,42]
print(list2,type(list1))
list4 = list([100,320,323])
print(list4)
list4.append(501) #added at the end 1 element
list4.extend([601,701,801]) # add more than one element 
list4.insert(0,51)
print(list4)
list4.remove(601)
list4.pop()
list4.pop(4)
del list4[1]
