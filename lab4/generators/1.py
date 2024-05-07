def sqr(n):
    for i in range(1,n+1):
        yield(i*i)
a=int(input())
for i in sqr(a):
    print(i)