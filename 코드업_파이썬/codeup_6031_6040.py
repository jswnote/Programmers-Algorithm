'''
6031번 - 정수 입력받아 유니코드 문자로 변환하기
c = int(input())
print(chr(c))
'''

'''
6032번 - 정수 하나를 입력받아 부호 바꾸기
n = input()
n = int(n)
print(-n)
'''

'''
6033번 - 문자 1개를 입력받아 다음 문자 출력하기
n = ord(input())
n = n + 1
print(chr(n))

ord - 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환합니다.
chr - 하나의 정수를 인자로 받고 해당 정수에 해당하는 유니코드 문자를 반환합니다.
'''

'''
6034번 - 정수 2개를 입력받아 차 계산하기
a, b = input().split()
a = int(a)
b = int(b)
print(a - b)
'''

'''
6035번 - 실수 2개를 입력받아 곱 계산하기
a,b = map(float, input().split())
print(a * b)
'''

'''
6036번 - 단어 여러번 출력하기
a, b = input().split()
b = int(b)

print(a*b)
'''

'''
6037번 - 문장 여러번 출력하기
a = int(input())

b = input()

print(b * a, sep = ' ')
'''

'''
6038번 - 정수 2개를 입력받아 거듭제곱 계산하기
a,b = map(int, input().split())

print(a**b)
'''

'''
6039번 - 실수 2개를 입력받아 거듭제곱 계산하기
a,b = map(float, input().split())

print(a**b)
'''

'''
6040번 - 정수 2개를 입력받아 나눈 몫 계산하기
a, b = map(int, input().split())

print(a//b)
'''