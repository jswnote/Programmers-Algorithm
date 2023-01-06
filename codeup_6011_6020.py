'''
6011번 - 실수 입력받아 출력하기 
f = (input())
f = float(f)
print(f)
#그냥 바로 input()함수를 사용하면 input함수는 무조건 type(f)가 str 그래서 float형으로 바꿔줘야함.
#이렇게 해도 되네.
f = float(input())
print(type(f))
'''

'''
6012번 - 2개의 정수를 입력받아 그대로 출력하기
a = input()
b = input()

print(a)
print(b)
'''

'''
6013번 - 2개의 문자를 입력받아 줄바꿔 출력하기
a = input()
b = input()

print(b)
print(a)
# 밑에 처럼도 될듯
a = input()
b = input()
print(a,b,sep= '\n')
'''

'''
6014번 - 실수 1개를 입력받아 3번 출력하기
f = float(input())

print(f)
print(f)
print(f)
'''

'''
6015번 - 정수 2개를 입력받아 그대로 출력하기
입력 = 1 2
출력 = 
1
2
a, b = input().split()

print(a)
print(b)
'''

'''
6016번 - 문자 2개를 입력받아 출력하기
a, b = input().split()
print(b, a)
'''


'''
6017번 - 문장 1개를 입력받아 3번 출력하기
a = input()
print(a, a, a)
'''

'''
6018번 - 시간 입력받아 그대로 출력하기
a, b = input().split(':')

print(a, b, sep=':')
#문자열.split(sep = '', maxsplit = ''), maxsplit = 분할횟수
#sep은 분류기호를 의미. print에서도 sep 구분자역할(기본값은 띄어쓰기). print에는 end = '\n'이 디폴트값.
'''


'''
#6019번 - 연원일 입력받아 순서바꿔 출력하기.
y,m,d = input().split('.')
print(d,m,y,sep='-')
'''

'''
#6020번 - 주민번호 입력받아 형태 바꿔 출력하기
a,b = input().split('-')
print(a,b,sep='')
'''