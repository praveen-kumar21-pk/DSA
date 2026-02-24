
# def convert(n):
#     if n<=0:
#         return 0
#     return convert(convert(n-1))
# n=int(input(" enter a number :"))
# print(convert(n))
def convert(n):
    if n <= 0:
        return 0
    return n + convert(n - 1)

n = int(input("Enter a number: "))
print(convert(n))
