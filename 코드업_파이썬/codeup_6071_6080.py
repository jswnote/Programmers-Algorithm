'''
6071번 - 0입력될 때까지 무한 출력하기
l = []
while True:
    a = int(input())
    l.append(a)
    if a == 0:
        break
for i in l:
    if i == 0:
        pass
    else:
        print(i, sep='\n')


모범답안(별론데)
while True:
    a = int(input())
    
    if (a == 0):
        break
    
    print(a)
'''

'''
6072번 - 정수 1개를 입력받아 카운트다운 출력하기1
a = int(input())

while True:
    if a != 0:
        print(a)
        a -= 1
    else:
        break
        
모범답안
a=int(input())

while a!=0:
    print(a)
    a=a-1
'''

'''
6073번 - 정수 1개를 입력받아 카운트다운 출력하기2
a = int(input())

while True:
    if a > 0:
        a -= 1
        print(a)
    elif a == 0:
        break
'''

'''
6074번 - 문자 1개를 입력받아 알파벳 출력하기
(6030번 참고)
c = ord(input())
t = ord('a')

while t<=c:
    print(chr(t), end = ' ')
    t += 1
'''

'''
6075번 - 정수 1개를 입력받아 그 수까지 출력하기1
a = int(input())

for i in range(a+1):
    print(i)
    
    
for i in range(n) :    #range(n)에 들어있는(in) 각각의 수에 대해서(for) 순서대로 i에 저장해 가면서... 
이때의 for는 각각의 값에 대하여... 라는 for each 의 의미를 가진다고 생각할 수 있다.
'''

'''
6076번 - 정수 1개를 입력받아 그 수까지 출력하기2
위와 동일
'''

'''
6077번 - 짝수 합 구하기
a = int(input())
l = []
for i in range(a+1):
    if i % 2 == 0:
        l.append(i)
    else:
        pass

k = 0
for i in l:
    k += i

print(k)
'''

'''
6078번 - 원하는 문자가 입력될 때까지 반복 출력하기
l = []
while True:
    a = input()
    l.append(a)
    if a == 'q':
        break
for i in l:
    print(i, sep='\n')
'''

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

'''
6080 - 주사위 2개 던지기
a,b = map(int, input().split())

for i in range(a+1):
    if i == 0:
        pass
    else:
        for j in range(b+1):
            if j == 0:
                pass
            else:
                print(i,j,sep = ' ')
                
모법답안 -
n,m=input().split()

n=int(n)
m=int(m)

for i in range(1, n+1) :
  for j in range(1, m+1) :
    print(i, j)
'''