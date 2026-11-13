class LLNode:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.first = None

    def prepend(self, value):
        node = LLNode(value)
        node.next = self.first
        self.first = node

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

    def append(self, value):
        if self.first == None:
            self.first = LLNode(value)
        else:
            current = self.first
            while current.next != None:
                current = current.next
            current.next = LLNode(value)

    def remove(self, value):
        previous = None
        current  = self.first
        while current != None and current.value != value:
            previous = current
            current = current.next
        if current != None:
            if previous != None:
                previous.next = current.next
            else:
                self.first = current.next

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

class Sorted(LinkedList):
    def insert(self, newval):
        if self.first == None:
            self.first = LLNode(newval)
        else:
            smallestval = self.first.value
            current = self.first
            if smallestval >= newval:
                self.prepend(newval)
            while current:
                if current.next is None and current.value < newval:
                    self.append(newval)
                elif current.value < newval and current.next.value > newval:
                    prevnode = current
                    newnode = LLNode(newval)
                    newnode.next = prevnode.next
                    prevnode.next = newnode 
                current = current.next
        



