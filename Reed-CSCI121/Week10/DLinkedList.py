class DLLNode:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None


class DLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
#Write the prepend, append, and remove methods of DLinkedList so that they modify both next and prev 
#when nodes are linked and unlinked with these methods. 
#They should also modify the first and last references in cases where those parts of the 
#list structure change.
#First = lefthand side, Last = Righthand side
    def prepend(self, value):
        node = DLLNode(value)
        if self.first ==None:
            self.first = node
            self.last = self.first
        else:
            previous = self.first
            node.next = previous
            previous.prev = node
            self.first = node

    def append(self, value):
        if self.first == None:
            self.first = DLLNode(value)
            self.last = self.first
        else:
            node = DLLNode(value)
            current = self.first
            while current.next != None:
                current = current.next
            current.next = node
            node.prev = current
            self.last = node

    def remove(self, value): #the 'next' linked list is shorter than the 'prev' linked list. (0,1,2,3) > (1,2,3)
        previous = None #Try removing at middle, not-completely middle, removing at end
        current  = self.first
        while current != None and current.value != value:
            previous = current
            current = current.next
        if current != None:
            if previous != None: #There exists something before this
                if current.next == None: #Checking if the spot being removed is the last in the list
                    previous.next=None
                    self.last = previous
                else:
                    spot = current.next
                    previous.next, spot.prev = spot, previous
                    current.prev, current.next = None, None 
                    #current.prev = None

            else: #PREV IS NONE
                if self.length() >1:
                    spot = current.next
                    self.first = spot
                    spot.prev, current.next = None, None 
                else:
                    #Only one value...
                    self.first, self.last = None, None





    def contains(self, value):
        current = self.first
        while current != None:
            if current.value == value:
                return True
            current = current.next
        return False

    def as_string(self):
        if self.first == None:
            return "<>"
        else:
            s = "<" + str(self.first.value)
            current = self.first.next
            while current != None:
                s = s + ", " + str(current.value)
                current = current.next
            s = s + ">"
            return s

    def length(self):
        count = 0
        current = self.first
        while current != None:
            count = count + 1
            current = current.next
        return count

    def is_empty(self):
        return (self.first == None)

    def display(self):
        print(self.as_string())

    def __str__(self):
        return self.as_string()

    def __repr__(self):
        return self.as_string()

    def __bool__(self):
        return not self.is_empty() 

    def sum(self):
        sumallval = 0
        if self.length() >= 1:
            currentspot = self.first
            while currentspot.next is not None:
                sumallval += currentspot.value
                currentspot = currentspot.next
            sumallval += currentspot.value

        return sumallval

    def count(self,value):
        current = self.first
        count = 0
        while current:
            if current.value == value:
                count+=1
            current = current.next
        return count

    def apply(self, function):
        current = self.first
        while current:
            current.value = function(current.value)
            current = current.next

    def remove_all(self, valuetoremove):
        current = self.first
        while current:
            if current.value == valuetoremove:
                self.remove(current.value)
            current = current.next

    def insert_at(self, index, value):
        # The first index should be an integer that is from 0 up to and including the length of the list. 
        #The second value can be any integer. 
        #The method should insert that value into the linked list at the position given by index. 
        #If 0, it should go in the front of the list. 
        #If 1 it should be placed just after the first item, and so on.
        if index == 0:
            self.prepend(value)
        elif index == self.length():
            self.append(value)
        else:
            node = DLLNode(value)
            count = 1
            current = self.first
            while current != None and count != index:
                current = current.next
                count +=1
            later = current.next
            node.next, current.next = later, node
            node.prev, later.prev = current, node 
