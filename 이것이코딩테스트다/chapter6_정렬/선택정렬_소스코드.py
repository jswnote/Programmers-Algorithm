array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)): # 0~9까지
    min_index = i #처음 0
    for j in range(i+1, len(array)): # 1~9까지
        if array[min_index] > array[j]: #array[0] > array[1], 처음 7 > 5 True. 두 번째 array[1] > array[2] False. 
            min_index = j # min_index = 1, 다음 min_index = 3
            # 결국 최소 min_index 찾는 방법.
    array[i], array[min_index] = array[min_index], array[i]
    #스와프 : 특정한 리스트가 주어졌을 때 두 변수의 위치를 변경하는 작업.
    
 
print(array)  

