def even(n):
    for i in range(0,n+1,2):
        yield(i)
a=int(input())
for i in even(a):
    print(i)