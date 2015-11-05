__author__ = 'jonet5'
class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node

class Linked_List:
    #gives head a value
    def __init__(self, head = None):
        self.head = head

    #adds a new node and sets it to the head
    def insert(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    #reverse the linked list by iterating through them and changing pointers
    def reverse(self):
        current = self.head
        previous = None
        nxt = None
        #while the next node has a value keep going
        while current.next_node != None:
            nxt = current.get_next()
            current.set_next(previous)
            previous = current
            current = nxt
        #sets last value to point to the 2nd last
        nxt.set_next(previous)
        #sets the last value as the head
        self.head = nxt
        
#prints out the linked list
def prnt():
    print list.head.get_data()
    nxt = list.head.get_next()
    while nxt.get_next() != None:
        print nxt.get_data()
        nxt = nxt.get_next()
    print nxt.get_data()

list = Linked_List()
#populate the list
for i in range(20):
    list.insert(i)
print "forward"
prnt()
list.reverse()
print "reverse"
prnt()