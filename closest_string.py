from difflib import get_close_matches
for _ in range(int(input())):
    n,k=map(int,input().split())
    poss=[]
    to_find=[]
    for i in range(n):
        poss.append(input())
    for j in range(k):
        to_find.append(input())
    #print(poss)
    #print(to_find)
    for l in range(k):
        print(get_close_matches(to_find[l],poss,1)[0])
        


