'''
큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 특징이다.
예를 들어 순서대로 2,4,5,4,6으로 이루어진 배열이 있을 떄 M이 8이고, K가 3이라고 가정하자.
이 경우 특정한 인덱스의 수가 연속해서 세 번까지만 더해질 수 있으므로 큰 수의 법칙에 따른 결과는 6+6+6+5+6+6+6+5인 46이 된다.
단, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다.
첫쨰 줄에 N(2~1000), M(1~10000), K(1~10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단 각각의 자연수는 1 이상 10000 이하의 수로 주어진다.
입력으로 주어지는 K는 항상 M보다 작거나 같다.

입력
5 8 3
2 4 5 4 6

출력 46 6665666
'''

N,M,K = map(int, input().split())

N_list = list(map(int,input().split()))

N_list.sort()

total = 0

for i in range(M):
    if i % (K+1) != 0:
        total += N_list[N-1]
    elif i % (K+1) == 0:
        total += N_list[N-2]
    

print(total)

