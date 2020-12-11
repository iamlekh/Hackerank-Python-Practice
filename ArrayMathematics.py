import numpy


n,m = map(int,input().split())
ar1 = []
ar2 = []
for i in range(n):
    tmp = list(map(int,input().split()))
    ar1.append(tmp)
for i in range(n):
    tmp = list(map(int,input().split()))
    ar2.append(tmp)
a = numpy.array(ar1)
b = numpy.array(ar2)

print(numpy.add(a, b))      
print(numpy.subtract(a, b))    
print(numpy.multiply(a, b))
print(a//b)
print(numpy.mod(a, b))
print(numpy.power(a, b))        
