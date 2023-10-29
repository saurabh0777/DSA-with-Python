class node:
    def  __init__(self,data):
         self.data = data
         self.ref = None

class LinkedList:

    def __init__(self):
        self.head = None

    def printLL(self):

        if self.head ==None:
            print("Linked List is empty")


LL = LinkedList()
LL.printLL()
