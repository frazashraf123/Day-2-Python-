#Q1.
s = input()
l = len(s)
i = 0
countLetter = 0
countWord = 0
while(i<l):
    if((s[i] >= 'a' and s[i] <='z') or (s[i] >= 'A' and s[i]<='Z')):
        countLetter+=1
    elif(s[i]>='0' and s[i]<='9'):
        countWord+=1
    i+=1    
l = []
l.append(countLetter)
l.append(countWord)
print(l)     
"OR"
def f1(s):
    l=0
    d=0
    #l =[]
    for i in s:
        if(i.isalpha()):
            l+=1
        elif(i.isdigit()):
            d+=1
    return([w,d])
s=input()
print(f1(s))
