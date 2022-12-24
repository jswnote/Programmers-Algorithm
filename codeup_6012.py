#a,b = input().split()

#print(a)
#print(b)

#a,b = int(input().split())
#int 함수는 리스트를 정수형으로 바꿔줄 수 없다.

c, d = map(int,input().split())
print(c)
print(d)
#split 함수 각각의 값을 리스트로 나누어 줌.
print(type(c))

e = [1,2,3,4]
print(type(e[0]))