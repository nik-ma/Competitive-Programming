n,m = map(int,input().split(' '))
arr = input().split(' ')
a = set(input().split(' '))
b = set(input().split(' '))

happy = 0
for i in arr:
    if i in a:
        happy+=1
    if i in b:
        happy-=1
 
print(happy)

