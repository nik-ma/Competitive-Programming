n = int(input())
req = [int(x) for x in input().split()]
total = [int(i) for i in input().split()]
mini = []
for j in range(n):
    mini.append(total[j]//req[j])
print(min(mini))