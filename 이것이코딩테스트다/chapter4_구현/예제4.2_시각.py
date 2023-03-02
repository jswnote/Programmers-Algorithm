'''
시각 - 3이 들어가는 횟수
page 113

입력예시
5
출력예시
11475
'''

h = int(input())

count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            x = str(i) + str(j) + str(k)
            
            if '3' in x:
                count+=1
                

print(count)
# str 더하는게 포인트
# 시,분,초 for문 구조 포인트
