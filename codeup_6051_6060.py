#6056번 모범답안 봐야함.
#xor nand 연산자 공부.
#비트 연산자 뭔지 알아야 할 듯.
'''
6051번 - 정수 2개를 입력받아 출력하기4
a, b = input().split()
a = int(a)
b = int(b)
print(a!=b)
'''

'''
6052번 - 정수 입력받아 참 거짓 평가하기
n = int(input()) 
print(bool(n)) 

0은 false 다른 수는 true 인가? (o) 0 외의 숫자들은 모두 true로 판별.

n = bool(int(input()))
print(n)
'''

'''
6053번 - 참 거짓 바꾸기
a = bool(int(input()))
print(not a)
'''

'''
6054번 - 둘 다 참일 경우만 참 출력하기
a, b = input().split()
print(bool(int(a)) and bool(int(b))) 

a, b = map(int,input().split())

a = bool(a)
b = bool(b)

if a == b and a == True:
    print("True")

else:
    print("False")

#a==b만 하면 0, 0일 때도 True로 나옴. 따라서 조건부 a == True도 넣어줌.
'''

'''
6055번 - 하나라도 참이면 참 출력하기
a, b = input().split()
print(bool(int(a)) or bool(int(b))) 
'''

'''
6056번 - 참 거짓이 서로 다를 때만 참 출력하기

a,b = input().split()
c = bool(int(a)) 
d = bool(int(b)) 
if c==d:
    print(False)
else:
    print(True)
#(t,t) = f, (t,f) = t, (f,t) = t, (f,f) = f
내방식이 더 나은 것 같은데
print((c and (not d)) or ((not c) and d)) 
위가 xor 연산자인데 밑바닥부터 딥러닝 책 참고해야 할듯.


a, b = map(int, input().split())

if (bool(a) ^ bool(b) == True):
    print("True")
else:
    print("False")

위와 같이 하기도 함.
'''

'''
6057번 - 참 거짓이 서로 같을 때만 참 출력하기 
a,b = input().split()
c = bool(int(a)) 
d = bool(int(b)) 
if c==d:
    print(True)
else:
    print(False)
'''

'''
6058번 - 둘 다 거짓일 경우만 참 출력하기
a,b = input().split()
c = bool(int(a)) 
d = bool(int(b)) 

if c==d and c==False:
    print(True)
else:
    print(False)

'''

'''
6059번 - 비트단위로 NOT하여 출력하기
a = int(input())

print(~a)
'''

'''
6060번 - 비트단위로 AND 하여 출력하기
a, b = map(int, input().split())

print (a & b)
'''

