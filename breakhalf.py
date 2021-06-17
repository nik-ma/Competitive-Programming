tc,s=map(int,input().split())
for _ in range(tc):
    n=int(input())
    chef=[int(i) for i in input().split()]
    defender=[int(i) for i in input().split()]
    chef.sort()
    defender.sort()
    ontable={chef[0]}
    for i in range(n):
        if chef[i] not in ontable:
            print("NO")

            break
        if defender[i]<=chef[i]:
            print("NO")
            break
        else:
            ontable.add(defender[i])
    else:
        print("YES")



