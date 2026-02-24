# items = input("enter elements by spaces : ").split()
# target = input("enter the element to be saerched : ")
# found=False
# for i in range(len(items)):
#     if items[i] == target:
#         print(f"element found at indec:{i}")
#         found=True
#         break
# if not found:
#     print(f"element not found in the list")    
items = input("enter elements by spaces : ").split()
target = input("enter the element to be searched : ")

for i in range(len(items)):
    if items[i] == target:
        print(f"element found at index: {i}")
        break
else:
    print("element not found in the list")
