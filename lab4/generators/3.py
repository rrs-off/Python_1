def generator(n):
    for i in range(1,n+1):
        if i%3==0 and i%4==0:
            yield(i)
a=int(input())
for i in generator(a):
    print(i)
