n,l,r,x=map(int,input().split())
num=list(map(int,input().split()))
ans=0
for i in range(0,2**n):
    st=bin(i)[2:]
    st='0'*(n-len(st))+st
    # print(st)
    if st.count('1')>=2:
        pt=[]
        for i in range(len(st)):
            if st[i]=='1':
                pt.append(num[i])
        # print(pt)
        if sum(pt)<=r and sum(pt)>=l and max(pt)-min(pt)>=x:
            ans+=1
print(ans)
            
