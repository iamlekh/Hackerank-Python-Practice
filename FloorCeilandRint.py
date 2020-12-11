import numpy


a1 = list(map(float,input().split(' ')))
a2 = numpy.array(a1)
numpy.set_printoptions(legacy='1.13')
print(numpy.floor(a2))
print(numpy.ceil(a2))
print(numpy.rint(a2))

