s=input()
length=len(s)
string=''
l=[]
count=1
i=0
for i in range(length-1):
    if s[i]==s[i+1]:
        count+=1
    else:
        
        print(((count)),s[i],end=" ")
        count=1
print((count,s[i]),end=" ")