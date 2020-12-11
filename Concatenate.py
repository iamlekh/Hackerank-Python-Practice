import numpy
row1,row2, col = list(map(int, input().split(" ")))

l1 =[]
l2 =[]
for i in range(row1):
    l1.append(list(map(int, input().split(" "))))
for i in range(row2):
    l2.append(list(map(int, input().split(" "))))

    
a = numpy.array(l1)
b= numpy.array(l2)

print(numpy.concatenate((a,b),axis = 0))

