a = int(input())
b = list(map(str, input().split()))


print(all(int(i)>0 for i in b) and any(k==k[::-1] for k in b))