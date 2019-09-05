class Node:
    def __init__(self,data):
        self.data=data
        self.link=None
def insertL(data,head):
    n = Node(data)
    if head == None:
        head = n
        return head
    a = head
    while a.link!=None:
        a = a.link
    a.link = n
    return head
def insertF(data,head):
    n = Node(data)
    if head == None:
        head = n
        return head
    a = head
    head = n
    n.link = a
    return head
def deleteL(head):
    if head == None:
        return head
    a = head
    while a.link != None:
        pre = a
        a = a.link
    pre.link = None
    return head
def deleteF(head):
    if head == None:
        return head
    a = head
    head = a.link
    return head
def display(head):
    b = head
    while b != None:
        print(b.data)
        b = b.link
def merge(head,head1):
    a = head
    while a.link != None:
        a = a.link
    a.link = head1
    return head

head = None
head = insertL(1,head)
head = insertL(2,head)
head = insertL(3,head)
head = insertF(0,head)
head = deleteL(head)
head = deleteF(head)
display(head)
print()
head1 = None
head1 = insertL(4,head1)
head1 = insertL(5,head1)
head1 = insertL(6,head1)
display(head1)
print()
head = merge(head,head1)
display(head)