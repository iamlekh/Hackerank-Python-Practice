n = int(input())

def is_leap(year):
    return (year%4 ==0 and (year%100 != 0 or year%400 ==0))


if (1900<=n<=10**5):
    print(is_leap(n))

