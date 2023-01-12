'''
6061번 - 비트단위로 or하여 출력하기
a, b = map(int, input().split())

print (a | b)
'''

'''
6062번 - 비트단위로 xor하여 출력하기
a, b = map(int, input().split())

print (a ^ b)
'''

'''
6063번 - 정수 2개를 입력받아 큰 값 출력하기
a, b = map(int, input().split())
l = [a,b]
print(max(l))
'''

'''
6064번 - 정수 3개를 입력받아 가장 작은 값 출력하기
a, b, c= map(int, input().split())
l = [a,b,c]
print(min(l))

모범답안 1
a, b, c = input().split()
a = int(a)  #변수 a에 저장되어있는 값을 정수로 바꾸어 다시 변수 a에 저장
b = int(b)
c = int(c)

d = a if a<b else b
e = d if d<c else c

print(e)

모범답안 2
a, b, c = map(int, input().split())

print(min(a,b,c))
'''


'''
6065번 - 정수 3개를 입력받아 짝수만 출력하기
a, b, c = map(int, input().split())

l = [a,b,c]

for i in l:
    if i%2 == 0:
        print(i)
'''

'''
6066번 - 정수 3개를 입력받아 짝/홀 출력하기
a, b, c = map(int, input().split())

l = [a,b,c]

for i in l:
    if i%2 == 0:
        print('even')
    else:
        print('odd')
'''

'''
6067번 - 정수 1개를 입력받아 분류하기

a = int(input())

if a > 0:
    if a % 2 == 0:
        print('C')
    else:
        print('D')

else:
    if a % 2 == 0:
        print('A')
    else:
        print('B')
'''

'''
6068번 - 점수 입력받아 평가 출력하기
a = int(input())

if a >= 90:
    print('A')
elif a >= 70 and a < 90:
    print('B')
elif a >= 40 and a < 70:
    print('C')
else:
    print('D')
'''

'''
6069번 - 평가 입력받아 다르게 출력하기
a = input()
if a == 'A':
    print('best!!!')
elif a == 'B':
    print('good!!')
elif a == 'C':
    print('run!')
elif a == 'D':
    print('slowly~') 
else:
    print('what?')   
'''

'''
6070번 - 월 입력받아 계절 출력하기

a = int(input())

if a == 1 or a == 2 or a == 12:
    print('winter')
elif a == 3 or a == 4 or a == 5:
    print('spring')
elif a == 6 or a == 7 or a == 8:
    print('summer')
elif a == 9 or a == 10 or a == 11:
    print('fall')
'''