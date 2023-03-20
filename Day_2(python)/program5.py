
#Question 4.
def fun(st):
    if(st[-3:] == "ing"):
        return st+"ly"
    elif(len(st)<3):
        return st
    else:
        return st+"ing"

st = input()
print(fun(st))
