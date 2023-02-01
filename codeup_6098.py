a = []
m, n = map(int,input().split())

for i in range(m):
    line = []
    for j in range(n):
        line.append(int(input()))
    
    a.append(line)
        
        
print(a)