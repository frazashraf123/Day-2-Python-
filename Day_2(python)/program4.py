#Question 3
def fun(st):
    if (len(st)<2):
        print("-1")
    else:
        print(st[0:2]+st[-2:])
st = input()
fun(st)
