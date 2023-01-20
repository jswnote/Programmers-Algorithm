'''
6079번 - 언제까지 더해야 할까?
a = int(input())
t = 0
s = 0
while s < a:
    t += 1
    s += t
    
print(t)
'''