for _ in range(int(input())):
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
            string+=s[i]+str(count)
            count=1


    string+=s[i]+str(count)


    if len(string)>=length:
        print("NO")
    else:
        print("YES")

