import sys
for _ in range(int(input())):
    n,q=map(int,input().split())
    s=input()
    alpha=set(s)
    num=[]
    for i in alpha:
        num.append(s.count(i))
    for _ in range(q):
        p=sys.stdin.readline()
        p=int(p)
        for i in num:
            if num-p>=0:
                sum+=num-p
        sys.stdout.write(str(sum))
        sys.stdout.write("\n")