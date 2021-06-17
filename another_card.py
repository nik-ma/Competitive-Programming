for _ in range(int(input())):
    chef,rick=map(int,input().split())
    if chef%9==0:
        chef_n=chef//9
    elif chef%9!=0:
        chef_n=chef//9+1
    if rick%9==0:
        rick_n=rick//9
    elif rick%9!=0:
        rick_n=rick//9+1
    if chef_n==rick_n:
        print(1,rick_n)
    elif chef_n>rick_n:
        print(1,rick_n)
    else:
        print(0,chef_n)
    
