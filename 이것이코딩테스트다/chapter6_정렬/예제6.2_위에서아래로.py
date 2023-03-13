N = int(input())
l = []
for i in range(N):
    i = int(input())
    l.append(i)
    
result = sorted(l, reverse=True)

for j in result:
    print(j, end = ' ')