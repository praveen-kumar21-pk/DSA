# items = input("Enter numbers separated by space: ").split()
# for i in range(len(items)):
#     items[i] = int(items[i])
# items.sort()
# print("Sorted list:", items)
def show(n):
    if n == 0:        # Base case
        return
    print(n)
    show(n - 1)       # Recursive call

show(5)
