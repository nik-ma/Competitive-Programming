# Function to perform dfs and update the tree 
# such that every node's weight is the sum of 
# the weights of all the nodes in the sub-tree 
# of the current node including itself 
#mini = 2**32
def dfs(node, parent): 
    global mini, graph, weight,peop,days,j
    #print(weight[node])
    weight[node-1]-=min(weight[node-1],peop)
    
    for to in graph[node]:  
        if (to == parent):  
            continue
        dfs(to, node)  
def remove_edges(node, parent): 
    global mini, graph, weight,peop
    #print(weight[node])
    
        #print(mini,weight[node])
    for to in graph[node]:  
        graph[to].remove(node)
        graph[node].remove(to)
# Function to find the node
# having minimum sub-tree sum 

for _ in range(int(input())):
    global mini,peop,j
    mini=2**32
    n=int(input())
    global graph
    graph = [[] for i in range(n+1)]  
    global weight,days
     
    for i in range(1,n):
        u,v=map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    #ans = 0
    nodes_to_travel=[int(x) for x in input().split()]
    people=[int(x) for x in input().split()]
    
        
    fruits=[int(x) for x in input().split()]
    weight=fruits[:]
    
    #print(weight)
    #print(graph)
    days=[0]*(n+1)
    j=0
    visited=[0]*(n+1)
    for i in range(len(nodes_to_travel)):
   
        if weight[nodes_to_travel[i]-1]==0:
            continue
        peop=people[nodes_to_travel[i]-1]
        dfs(nodes_to_travel[i],nodes_to_travel[i])
        #mini=min(dfs(nodes_to_travel[i],nodes_to_travel[i]),people[nodes_to_travel[i]-1])
        
        for k in nodes_to_travel:
            if weight[nodes_to_travel[i]-1]!=0:
                days[nodes_to_travel[i]]=-1

            
            if weight[k-1]==0 and visited[k]!=1:
                days[k]=j+1
                visited[k]=1
        j+=1

        #dfs2(nodes_to_travel[i],nodes_to_travel[i])
        
        


        remove_edges(nodes_to_travel[i],nodes_to_travel[i])
        mini=2**32
    for i in range(1,len(nodes_to_travel)+1):
        print(days[i],end=" ")
    #print(graph,weight,nodes_to_travel,days)
    print()
    
    

    
  
    
    
