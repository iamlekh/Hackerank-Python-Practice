a = []
b = set()
for _ in range(int(input())):
    name = input()
    mark = float(input())
    a.append([name, mark])
    b.add(mark)

sl = sorted(b)[1]
x=[]
for n,m in a:
    if m == sl:
        x.append(n)


x= sorted(x)
for i in x:
    print(i)
print(x)


