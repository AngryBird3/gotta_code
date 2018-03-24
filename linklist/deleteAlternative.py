'''
Created on Dec 16, 2012

@author: dharadarji

Given a Singly Linked List, starting from the second node delete all alternate nodes of it.
'''

class List:
    def __init__(self, data, nextnode):
        self.data = data
        self.next = nextnode
        
    def hasNext(self):
        return self.next != None
    
    def getNext(self):
        return self.next
    
    def setNext(self, nextnode):
        self.next = nextnode
        
    def setData(self, data):
        self.data = data
    
    def getData(self):
        return self.data
    
node15 = List(5, None)
node14 = List(4, node15)
node13 = List(3, node14)
node12 = List(2, node13)
node1 = List(1, node12)

def deleteAlternative(head):
    if head == None:
        return
    prevNode = head
    nextNode = head.next
    while(nextNode != None):
        prevNode.next = nextNode.next
        'free nextNode'
        prevNode = prevNode.next
        if prevNode != None:
            nextNode = prevNode.next
     
def printList(head):
    while head!=None:
        print head.data
        head = head.getNext()

deleteAlternative(node1)
printList(node1)

    