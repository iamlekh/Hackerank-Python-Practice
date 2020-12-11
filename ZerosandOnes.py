import numpy

n = tuple(list(map(int, input().split(" "))))
print(numpy.zeros(n, dtype = numpy.int))
print(numpy.ones(n, dtype = numpy.int))