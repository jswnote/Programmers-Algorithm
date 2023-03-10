array = list(map(int,input().split()))


def quick_sort(array, start, end):
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end
    
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        
        while right > start and array[right] >= array[left]:
            right -= 1
            
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
            
        else:
            array[left], array[right] = array[right], array[left]
    
    
    quick_sort(array, start, right - 1)
    quick_sort(array, right+1, end)
    
    
quick_sort(array, 0, len(array) - 1)

print(array)