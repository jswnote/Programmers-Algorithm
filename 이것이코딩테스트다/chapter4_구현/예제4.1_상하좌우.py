'''
page 110

입력예시 
5
R R R U D D

출력예시
3 4
'''

N = int(input())
plans = input().split()

x, y = 1, 1
# 행렬로 표시
dx = [0,0,-1,1]
dy = [-1, 1, 0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]: #하나하나씩 대조
            nx = x + dx[i]
            ny = y + dy[i]
        
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
        
    x, y = nx, ny
        
print(x, y)

# input().split() = 리스트로 반환
# 리스트로 저렇게 dx, dy를 나누는게 포인트
# 계속 복습하자.
        