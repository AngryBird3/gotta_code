'''
Created on Dec 16, 2012

@author: dharadarji

Given v v very large num, cant store in a "variable", add them with link list
O(n)
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
    
node14 = List(3, None)
node13 = List(9, node14)
node12 = List(9, node13)
node1 = List(9, node12)

node24 = List(0, None)
node23 = List(9, node24)
node22 = List(9, node23) 
node2 = List(0, node22)

def addTwoList(head1, head2):
    total = head1.data + head2.data
    newnode = List(total%10, None)
        
    carry = total / 10
    newhead = newnode
    head1 = head1.next
    head2 = head2.next
    while head1!=None and head2!=None:
        total = head1.data + head2.data + carry
        carry = 0
        prevnode = newnode
        newnode = List(total % 10, None)
        prevnode.setNext(newnode)
        carry = total / 10
        head1 = head1.getNext()
        head2 = head2.getNext()

    #what if left with last carry, #join?
    if carry != 0:
        newnode.setData(newnode.data + carry * 10)
        
    print "Total: "
    while newhead!=None:
        print newhead.data
        newhead = newhead.getNext()

addTwoList(node1, node2)    
