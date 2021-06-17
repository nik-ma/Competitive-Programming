for _ in range(int(input())):
    s=input()
    for i in range(2,len(s),2):
        p1=s[0:(i//2)-1]
        p2=s[i:(i+1//2)-1]
        p3=s[:(i//2)-1]
        p4=s[0:(i//2)-1]