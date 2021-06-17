for _ in range(int(input())):
    string=input()
    cou=0
    i=0
    while i<len(string)-1:
        if string[i]=='x' and string[i+1]=='y':
            cou+=1
            i+=2
        elif string[i]=='y' and string[i+1]=='x':
            cou+=1
            i+=2
        else:
            i+=1
    print(cou)