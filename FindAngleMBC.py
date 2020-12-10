import math
AB = int(input())
BC = int(input())

o = round(math.degrees(math.atan2(AB, BC)))
print(str(o) + '°')