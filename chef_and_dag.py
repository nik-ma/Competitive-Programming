for _ in range(int(input())):
    n,k = map(int,input().split())
    graph = []

    for i in range(n):
        temp = []

        for j in range(n):
            if j == i:
                temp.append(0)
            else:
                temp.append(1)

        graph.append(temp)
    print(graph)

    for i in range(k):
        query = [int(i) for i in input().split()]
        for j in range(n):
             for k in range(j):
                 graph[query[j]-1][query[k] - 1] = 0
    print(graph)

