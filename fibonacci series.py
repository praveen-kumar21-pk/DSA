# write a code to generate fibonacci numbers using tree recursion till n elements 
def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)
n = int(input("enter the range :"))
for i in range(n):
    print(fib(i),end=' ')