m,n = map(int,input().split())
special =('!', '@', '#', '$', '%', '&')
matrix = []

for i in range(m):
    string = input()

    matrix.append(string)        
ans =""
for i in range(n):
    for j in range(m):
        if matrix[j][i] in special:
            ans+=' '
        else:
            ans+=matrix[j][i]
print(ans)