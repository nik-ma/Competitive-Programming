def gain(movie):
    movie.sort(reverse=True)
    ab = 0
    rs = [100,75,50,25]
    j = 0
    for i in movie:
        if i == 0:
            ab -=100
        else:
            ab += i*rs[j]
            j +=1
    return ab
def solve(arr):
    tagp = {0,1,2,3}
    sol = -100000000

    for i in tagp:
        ni = [arr[0][i]]
        bi = tagp - {i}
        for j in bi:
            y = ni + [arr[1][j]]
            cd = bi -{j}
            for k in cd:
                nik = y + [arr[2][k]]
                d = cd - {k}

                for l in d:
                    pt = nik + [arr[3][l]]
                    pr = gain(pt)
                    if pr > sol:
                        sol =pr
    return sol
Movd = {"A":0,"B":1,"C":2,"D":3}
timd = {"12":0,"3":1,"6":2,"9":3}
ans = 0
for _ in range(int(input())):
    N = int(input())
    arr = [[0,0,0,0] for i in range(4)]
    for i in range(N):
        m,t = input().split()
        arr[Movd[m]][timd[t]] += 1
    answer = solve(arr)
    print(answer)
    ans +=answer
print(ans)


