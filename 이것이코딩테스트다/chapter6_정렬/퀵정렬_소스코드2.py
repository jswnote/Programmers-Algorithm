array = [5,7,9,0,3,1,6,2,4,8]

def quick(array):
    
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    
    left = []
    right = []
    for i in tail:
        if i <= pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
            
    return quick(left) + [pivot] + quick(right)

print(quick(array))