#Question 5.
def fun(num):
    double = num*2
    if(len(str(num)) == len(str(double))):
        for i in str(num):
            if i not in str(double):
                return False
        return True
    return False        
num= int(input())
print(fun(num))
