marks = []
student = {}
for _ in range(int(input())):
    data = input().split(" ")
    mark = list(map(float, data[1:]))
    student[data[0]] = sum(mark)/len(mark)


print("%.2f"%round(student[input()],2))
