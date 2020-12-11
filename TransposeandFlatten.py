import numpy
row,col = list(map(int, input().split(" ")))

l =[]
for i in range(row):
    l.append(list(map(int, input().split(" "))))

    
a = numpy.array(l)
print(a.T)
print(a.flatten())  

