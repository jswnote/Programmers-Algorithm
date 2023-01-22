'''
6082번 - 3,6,9 게임의 왕이 되자
a = int(input())

for i in range(1, a+1):
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        print('X', end = ' ')
          
    else:
        print(i, end = ' ')

'''

'''
6083번 - 빛 섞어 색 만들기
a,b,c = map(int,input().split())
count = 0 

for i in range(a):
    for j in range(b):
        for k in range(c):
            print(i,j,k, sep = ' ')
            count += 1
            
print(count)
'''

'''
6085번 - 그림 파일 저장용량 계산하기
a,b,c = map(int,input().split())

d = a*b*c/8/1024/1024

print('%.2f'%d,"MB")
'''

'''
6087번 - 3의 배수는 통과
a = int(input())
for i in range(1, a+1):
    if i % 3 == 0:
        pass
    else:
        print(i, end = ' ')
'''

'''
6088번 - 수 나열하기1
a,b,c = map(int,input().split())

d = a + (c-1)*b
print(d)
'''

'''
6089번 - 수 나열하기2
a,b,c = map(int,input().split())
d = (a*(b**(c - 1)))
print(d)
'''

'''
6090번 - 수 나열하기3
a, b, c, d = map(int,input().split())

for i in range(1, d):
    a = (a * b) + c
    
print(a)
'''