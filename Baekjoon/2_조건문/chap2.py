'''
1330 - 두 수 비교하기
a, b = map(int, input().split())

if a > b:
    print('>')
elif a < b:
    print('<')
elif a==b:
    print('==')
'''

'''
9498 - 시험 성적
score = int(input())
if 90<= score and score <=100:
    print("A")
elif 80<= score and score <= 89:
    print("B")
elif 70<= score and score <= 79:
    print("C")
elif 60<= score and score <= 69:
    print("D")
else:
    print("F")
'''

'''
2753 - 윤년
a = int(input())

if (a % 4 == 0 and a % 100 != 0) or (a % 400 ==0):

    print(1)
else:
    print(0)
'''

'''
14681 - 사분면 고르기
x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print('1')
    else:
        print('4')
else:
    if y > 0:
        print('2')
    else:
        print('3')
'''

'''
2884 - 알람 시계
H, M = map(int, input().split())

if M < 45 :	# 분단위가 45분보다 작을 때 
    if H == 0 :	# 0 시이면
        H = 23
        M += 60
    else :	# 0시가 아니면 (0시보다 크면)
        H -= 1	
        M += 60
        
print(H, M-45)	
'''

'''
2525 - 오븐 시계
a, b = map(int, input().split())
c = int(input())

a = a + (c // 60)
b = b + (c % 60)


if b >= 60:
    a += 1
    b -= 60
if a >= 24:
    a -= 24
        
        
print(a, b)
'''

'''
2480 - 주사위 세개
a,b,c = map(int, input().split())

if (a==b and b==c and a==c):
    result = (1000*a) + 10000
    
if (a == b and b != c):
    result = (100 * a) + 1000
elif (a == c and b != c):
    result = (100 * a) + 1000
elif (b == c and a != c):
    result = (100 * b) + 1000
else:
    if a > b > c or a > c > b:
        result = a * 100
    elif b > a > c or b > c > a:
        result = b * 100
    elif c > a > b or c > b > a:
        result = c * 100

print(result)
'''
