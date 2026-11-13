class LLNode:
    def __init__(self, value):
        self.value = value
        self.next = None
# Stacks are often used to keep track of a set of things when, for some reason, 
#the "last thing in is the first thing out" behavior is the right organization for what you need to track. 
class Queue:

    def __init__(self):
        self.first = None
        self.last = None
# When the queue has several items, self.first should contain the node with the value 
#that's been sitting in the queue the longest. 
#This would be the value that was least recently added, the head item. 
#The next node after self.first should contain the value that was added after the "head", 
#and so on, all the way to the node at the end, which should contain the value most recently added. 
#The variable self.last should be that last node in the list.

    def enqueue(self, value):
        #places item into queue, at the back
        #Your code should replace 'pass'

        #When a value is added to the queue with enqueue, a new node should be placed at the end 
        #of the list, and self.last should be changed to refer to that new node. 
        if self.first == None:
            self.first = LLNode(value)
            self.last = self.first
        else:
            current = self.first
            while current.next != None:
                current = current.next
            current.next = LLNode(value)
            self.last = current.next


    def head(self):
        if self.first == None:
            return None
        else:
            return self.first.value

    def dequeue(self):
        #removes item from queue
        #dequeue instead removes the least recently added item from the queue
        #Your code should replace 'pass'

        #When a value is removed with dequeue the node referenced by self.first 
        #should be removed and self.first should change to the next node in the linked list.

        holdvalue = self.first.value
        
        count = 0
        current = self.first
        while current != None:
            count = count + 1
            current = current.next
        
        if count >1:
            self.first = self.first.next
        else:
            self.first = None
            self.last = None

        return holdvalue

