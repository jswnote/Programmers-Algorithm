#인덱싱은 문자열이나 리스트에 번호를 부여하는것이다.
'''
l = ['a','b','c']
for i in l:
    print(i)
'''

'''
6021번 - 단어 1개를 입력받아 나누어 출력하기
s = input()
for i in s:
    print(i)
'''

'''
6022번 - 연월일 입력받아 나누어 출력하기
s = input()
print(s[0:2],s[2:4],s[4:6], sep = ' ')
'''

'''
6023번 - 시분초 입력받아 분만 출력하기
a,b,c = input().split(':')
print(b)
'''

'''
6024번 - 단어 2개를 입력받아 이어붙이기
a, b = input().split()
print(a,b, sep = "")
'''

'''
#6025번 - 정수 2개를 입력받아 합 계산하기
a, b = input().split()
a = int(a)
b = int(b)
print (a + b)
'''

'''
#6026번 - 실수 2개를 입력받아 합 계산하기
a = input()
b = input()
a = float(a)
b = float(b)
print (a + b)
'''

'''
6027번 - 10진수 정수를 출력받아 16진수로 출력하기
a = input()
a = int(a)
print(format(a, 'x'))

#부가설명
format(value, '#b') = 10진수에서 2진수 변환
format(value, '#o') = 10진수에서 8진수 변환
format(value, '#x') = 10진수에서 16진수 변환
2진수 : 0b
8진수 : 0o
16진수 : 0x
#을 제거하면 숫자만 출력됨.
'''

'''
6028번 - 10진수 정수를 출력받아 16진수 대문자로 출력하기
a = input()
a = int(a)
print(format(a, 'X'))
'''

'''
6029번 - 16진 정수 입력받아 8진수로 출력하기
a = input()
a = int(a, 16)

print(format(a, 'o'))
'''

'''
6030번 - 영문자 1개를 입력받아 10진수로 출력하기

n = ord(input())
print(n)

#부가설명
n = ord(input())  #입력받은 문자를 10진수 유니코드 값으로 변환한 후, n에 저장한다.

ord( ) 는 어떤 문자의 순서 위치(ordinal position) 값을 의미한다.  
실제로 각각의 문자들에는 연속된 정수 값이 순서에 따라 부여 되어 있다. A:65, B:66, C:67 .... 
ord(c) : 문자 c 를 10진수로 변환한 값 

컴퓨터로 저장되고 처리되는 모든 데이터들은 2진수 형태로 정수화 되어야 하는데,
컴퓨터에 문자를 저장하는 방법으로 아스키코드(ASCII Code)나 유니코드(Unicode)가 자주 사용된다.

예를 들어, 영문 대문자 'A'는 10진수 값 65 로 표현하고, 
2진수(binary digit) 값 1000001 로 바꾸어 컴퓨터 내부에 저장한다. 

유니코드(unicode)는 세계 여러 나라의 문자를 공통된 코드 값으로 저장할 때 사용하는 표준 코드이다.
'''

'''
#파이썬에서 권장하지 않는 방법
s = [1, 3, 5]
for i in range(len(s)):
    print(s[i])
'''

'''
for v in s:
    print(v)
'''

'''
enumerate 
반복문 사용 시 몇 번째 반복문인지 확인이 필요할 수 있습니다. 이때 사용합니다.
인덱스 번호와 컬렉션의 원소를 tuple형태로 반환합니다.
t = [1,2,3,4,5]
for i, v in enumerate(t):
    print("index : {}, value: {}".format(i,v))
'''