n = int(input())
a = list(map(int, input().split()))

if (2<=n<=10):
    for i in a:
        if i in range(-101,101):
            b = sorted(a)
            m = max(b)
            while max(b) == m:
                b.remove(max(b))
print(max(b))