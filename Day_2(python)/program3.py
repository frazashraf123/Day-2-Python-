#Question 2.     
def fun(l,s):
    count = 0
    for i in range(len(l)-1):
        for j in range(i,len(l)):
            if l[i] + l[j] == s:
                count+=1
    return count
l = [int(x) for x in input().split(" ")]
s = int(input())
print(fun(l,s))
