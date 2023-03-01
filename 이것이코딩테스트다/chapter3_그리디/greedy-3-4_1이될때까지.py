'''
어떠한 수 N이 1이 될때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.
1. N에서 1을 뺸다.
2. N을 K로 나눈다.

page.99

입력
25 5
출력
2
'''

N, K = map(int, input().split())
count = 0
while True:
    if N % K == 0:
        N //= K
        count += 1
        if N == 1:
            break
        
    else:
        N -= 1
        count += 1
        if N == 1:
            break

print(count)
        
