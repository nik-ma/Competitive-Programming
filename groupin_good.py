for _ in range(int(input())):
    s=input()
    maxi=-1
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            kt=set(s[i:j])
            #print(kt,s[i:j])
            if 2*(len(kt))-1==(len(s[i:j])) or (2*len(kt))==len(s[i:j]) or len(kt)==1:
                if maxi<j-i:
                    maxi=j-i
    print(maxi)

            
