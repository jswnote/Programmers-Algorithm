'''
왕실의 나이트
page 115

입력예시
a1

출력예시
2
'''
input_data = input()
row = int(input_data[1]) # 행
column = int(ord(input_data[0])) - int(ord('a')) + 1 # 열

# 4.2와 같이 1,1 에서 시작하게 하기

steps = [ (-2,-1),(-2,1),(-1,-2),(-1,2),(1,2),(1,-2),(2,-1),(2,1)]

result = 0

for i in steps:
    new_row = row + i[0]
    new_column = column + i[1]
    print(new_row, new_column)
    
    if new_row >= 1 and new_row <= 8 and new_column <= 8 and new_column >= 1:
        result += 1
        
print(result)



#row, column 나누는게 핵심.
#str도 리스트처럼 인덱싱 할 수 있음.
#(row,column) = (1,1)에서 계속 계산해야하는데, row+= row로 하면 중첩이 되어버림.
#ord가 이렇게도 쓰일 수 있구나라는 생각이 드네.