import numpy

def arrays(arr):
    a =numpy.array(arr).astype(numpy.float)
    return a[::-1]
    
    
    
    
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)