'''

'''

h = int(input())

count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            x = str(i) + str(j) + str(k)
            
            if '3' in x:
                count+=1
                

print(count)
