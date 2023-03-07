from collections import deque

visited = [False] * 9

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

def bfs(graph, v, visited):
    visited[v] = True
    queue = deque([v])
    while queue: #while 리스트, 리스트의 데이터가 없을 때까지 while문 반복
        v = queue.popleft() #처음에 1만 있으니까
        print(v, end = ' ')
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
                
                
bfs(graph, 1, visited)
