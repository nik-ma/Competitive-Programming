for _ in range(int(input())):
    ni = {}
    n, p =  map(int, input().split())
    j = 0
    for i in input().split():
        ni[int(i)] = j
        j += 1

    arr = list(ni.keys())
    arr = sorted(arr, reverse = True)
    di = [0]*n
    ans = "NO"
    for i in arr:
        if p%i == 0:
            di[ni[i]] = p//i - 1
            p = i

        else:
            di[ni[i]] = p//i + 1
            ans = "YES"
            break
    if ans == "NO":
            print(ans)
    else:
            print(ans,end=" ")
            for i in range(n):
                print(di[i],end=" ")
            print()
