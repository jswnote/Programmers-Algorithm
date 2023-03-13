N = int(input())

result = []
for i in range(N):
    #튜플 형식으로 데이터 생성하는법 중요
    data = input().split()
    result.append((data[0], int(data[1])))
    

def setting(result):
    return result[1]


result = sorted(result, key=setting)

for j in range(len(result)):
    print(result[j][0], end = ' ')