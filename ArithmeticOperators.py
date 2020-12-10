a = int(input())
b = int(input())

x= 10**10

if (a<=x) and (b<=x):
    print(a+b)
    print(a-b if a>b else b-a)
    print(a*b)