#6095번 - 바둑판에 흰 돌 놓기

a = int(input())
b = []
for i in range(20):
    c = []
    for j in range(20):
        c.append(0)
    b.append(c)
    
for i in range(a):
    x,y  = input().split()
    b[int(x)-1][int(y)-1] = 1

for i in range(19): 
    for j in range(19):
      print(b[i][j], end=' ')
    
    print()
