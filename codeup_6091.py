'''
6091번 - 함께 문제 푸는 날
a,b,c = map(int,input().split())
d = 0
while True:
    d += 1
    if d % a == 0 and d % b == 0 and d % c == 0:
        break
    
print(d)
'''

'''
약수 구하기

list = []
a = int(input())
b = 0
for i in range(a):
    b += 1
    if a % b == 0:
        list.append(b)
        
print(list)

'''


    
    