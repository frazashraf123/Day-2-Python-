#Question 6.
t = (12,18,25,24,2,5,18,20,20,21)
def find_more():
    c=0
    l=list(t)
    avg = sum(l)/len(l)
    for i in l:
        if(i>avg):
            c+=1
    return (c/len(l))*100
def find_frequency():
    count=0
    freq=[]
    for i in range(26):
        count=0
        for y in t:
            if i==y:
                count+=1
        freq.append(count)
    return freq    
def sort():
    l=sorted(t) #returns list
    return l

print(find_more())    
print(find_frequency())
print(sort())
