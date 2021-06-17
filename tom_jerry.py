for _ in range(int(input())):
    tom_strength = int(input())
    if tom_strength%2!=0:
        print(tom_strength//2)
    else:
        while tom_strength%2==0:
            tom_strength=tom_strength//2
        print(tom_strength//2)



