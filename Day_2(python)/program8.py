def dict(d,l):
    list2=[]
    for i in l:
        list2.append(d[i])
    return list2
d={"merry":"good","christmas":"jul","and":"och","hapy":"gott","new":"nytt","year":"ar"}
#l = [int(x) for x in input().split(" ")]
l=["merry","christmas"]
print(dict(d,l))



def find(s,e,l):
    count=0
    for i in range(len(l)):
        sum=l[i]
        if(l[i]%2!=0):
            count+=1
            print(sum)
        for j in range(i+1,len(l)):
            sum=sum+l[j]
                                  
            if sum%2!=0:
                count+=1
                print(sum)
            
    return count
s=int(input())
e=int(input())
l=[int(x) for x in input().split(" ")]
print(find(s,e,l))

n1=int(input())
n2=int(input())
res=[]
for i in range(n1,n2+1):
    res.append(i)
print(res)





    










 
    










            




    
