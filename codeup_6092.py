'''
6092번 - 이상한 출석 번호 부르기1
#23명중에 총 몇 번 부를지 선언을 해주고 중복되어도 상관없음.

a = int(input()) # 몇 번 부를건지 선언.
b = input().split() # 부른 번호에 대해서 리스트를 생성. 하지만 각 원소 str type.
c = [] # 23명 중에 몇 번 학생을 몇 번 불렀는지 체크할 리스트 생성.


for i in range(a): #리스트 정수형으로.
    b[i] = int(b[i])
    
for i in range(24): #0으로 구성되어 있는 리스트 생성.
    c.append(0)

for i in range(a): 
    c[b[i]] += 1
    
for i in range(1,24):
   print(c[i], end = ' ')
'''

'''
6093번 - 이상한 출석 번호 부르기2
#23명중에 총 몇 번 부를지 선언을 해주고 중복되어도 상관없음. 이번에는 거꾸로 부르기.
a = int(input())
b = input().split()



for i in range(a):
    b[i] = int(b[i])
    
for i in range(1,a+1):
    print(b[-i], end = ' ')
'''

'''
6094번 - 이상한 출석 번호 부르기3
#가장 빠른 번호 찾기

a = int(input()) 
b = input().split()

for i in range(a):
    b[i] = int(b[i])
    
b.sort()

print(b[0])
'''