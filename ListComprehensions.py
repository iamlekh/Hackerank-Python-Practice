X = int(input())
Y = int(input())
Z = int(input())
N = int(input())

f = []

print([[a,b,c] for a in range(X+1) for b in range(Y+1) for c in range(Z+1) if a+b+c!=N])





