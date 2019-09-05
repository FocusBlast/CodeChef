class Node:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link
def Push(data,head):
        n = Node(data)
        if(head==Node):
            head = n
            return head
        n.link = head
        head = n
        return head
def Pop(head):

        if(head == None):
            print("List is null")
            return None
        head = head.link
        return head
def Display(head):
        while(head!= None):
            print(head.data, end = "")
            head =head.link
head = None
head = Push(2,head)
head = Push(5, head)
Display(head)
head = Pop(head)
print()
Display(head)
