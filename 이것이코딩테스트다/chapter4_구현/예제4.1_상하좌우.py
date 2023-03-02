'''
page 110

입력예시 
5
R R R U D D

출력예시
3 4
'''

N = int(input())
plan = input().split()

x, y = 1, 1
dx = [0,0,-1,1]
dy = [-1, 1, 0,0]
move_types = ['L','R','U','D']

for plan in plan:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
        
    x, y = nx, ny
        
print(x, y)

