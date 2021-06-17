n =int(input())
matrix =[]
for i in range(n):
    matrix.append([int(i) for i in input().split()])

dictionary = {-1:0}

for i in range(n):
    start,end=matrix[i][0],matrix[i][1]
    for j in range(start,end):
        counter=0
        if j in dictionary:
            counter=dictionary[j]
        dictionary[j]=counter+1
great=-1
for k in dictionary:
    if dictionary[k]>dictionary[great]:
        great =k

print(great)