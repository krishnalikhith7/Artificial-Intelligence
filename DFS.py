def dfs(graph,node):
    visited=[]
    stack=[]
    visited.append(node)
    stack.append(node)

    while stack:
        t=stack.pop()
        print(t, end=" ")


        for neighbor in graph[t]:
            if neighbor not in visited:
                visited.append(neighbor)
                stack.append(neighbor)

graph=eval(input('Enter graph: '))
s=int(input('Enter source: '))
dfs(graph,s)

