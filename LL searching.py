class node:
    def __init__(self, data):
        self.data = data
        self.next = None
def insert_end(head, value):
    new_node = node(value)
    if head is None:
        return new_node
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    return head
def search(head,key):
    pos = 1
    temp = head
    while temp.next:
        temp=temp.next
        pos+=1
    return -1
head = None
n = int(input("Enter number of nodes: "))
for i in range(n):
    val = int(input("Enter value: "))
    head = insert_end(head, val)
key=it(input("enter element to be searched"))        
p=search(head,key)
if p != -1:
    print("element fund at position,",p)
else:
    print("element not found !!!!")    