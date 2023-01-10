#6042번 다시 보기. 시프트 연산자.

'''
6041번 - 정수 2개를 입력받아 나눈 나머지 계산하기
a, b = map(int,input().split())

print(a%b)
'''

'''
6042번 - 실수 1개를 입력받아 소수점이하 자리 변환하기
a=input()
a=float(a)
print(format(a, ".2f"))

#format(수, ".2f") 를 사용하면 원하는 자리까지의 정확도로 반올림 된 실수 값을 만들어 준다. 
'''

'''
6043번 - 실수 2개를 입력받아 나눈 결과 계산하기
a, b = map(float,input().split())

print(format(a/b, ".3f"))
'''

'''
6044번 - 정수 2개를 입력받아 자동으로 출력하기
a, b = map(int,input().split())

print(a+b, a-b, a*b, a//b, a%b, format(a/b, ".2f"), sep='\n')
'''

'''
6045번 - 정수 3개를 입력받아 합과 평균 출력하기
a,b,c = map(int, input().split())

print(a+b+c, format((a+b+c)/3, ".2f"))
'''


'''
6046번 - 정수 1개를 입력받아 2배 곱해 출력하기
# 비트시프트연산
# 즉 x << n은 x * 2^n이라는 공식이 성립하게 되는 것이다.
a = input()
a = int(a)

print(a<<1)


시프트 연산자는 이동시키는 연산자인데 무엇을 이동시키냐면
2진수로 표현된 비트를 해당하는 방향으로 이동시키는 연산자가 되겠다.
10 >> 2라면
10진수의 정수 10을 2진수로 변환한 값을 오른쪽으로 2칸 이동한 것이고 00001010 -> 00101000
20 << 4라면
10진수의 정수 20을 2진수로 변환한 값을 왼쪽으로 4칸 이동한 것이다. 

'''

'''
6047번 - 2의 거듭제곱 배로 곱해 출력하기

a, b = map(int,input().split())

print(a<<b)
'''

'''
6048번 - 정수 2개를 입력받아 비교하기 1
a, b = input().split()
a = int(a)
b = int(b)
print(a<b)

#if문을 사용해도 되지만 모범답안은 위와 같다.
'''

'''
6049번 - 정수 2개를 입력받아 비교하기 2
a,b = map(int, input().split())

print(a==b)
'''

'''
6050번 - 정수 2개를 입력받아 비교하기 3
a,b = map(int, input().split())

print(b>=a)
'''


'''
'{인덱스0}, {인덱스1}'.format(값0, 값1)
"{}".format() 방식 말고도,
format(실수, ".표기할 자리수f")로 표기할 자리수를 지정한 문자열로 출력하실 수 있습니다.

a, b = map(float, input().split())

print('{:.2f}'.format(a/b))
'''
