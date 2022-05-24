# Student# 301-154-898
#Student: Bruno Cantanhede Morgado

# The node of a list   
class _Node: 

    def __init__(self, data):    
        self.data = data;    
        self.next = None;

    def __repr__(self):
        return str(self.data)

     
class CircularLinkedList:
    # Initially declaring head and rear pointer as null    
    def __init__(self):    
        self.head = _Node(None)    
        self.rear = _Node(None)    
        self.head.next = self.rear    
        self.rear.next = self.head    
        
    # This function will add the new node at the end of the list    
    def add(self,data):    
        newNode = _Node(data);    
        # Checks if the list is empty.    
        if self.head.data is None:    
            # If list is empty, both head and rear would point to new node   
            self.head = newNode    
            self.rear = newNode    
            newNode.next = self.head    
        else:    
            # rear will point to new node   
            self.rear.next = newNode    
            #New node will become new rear
            self.rear = newNode    
            # Since, it is circular linked list rear will point to head    
            self.rear.next = self.head    
     
    # # Returns the number of nodes in a circular list
    # def size_of_list(self):
    #     return self.num_of_nodes
    
    def clone(self):
        result = CircularLinkedList()
        current = self.head
        # Nothing to do if the list is empty
        if self.head is None:    
            print('List is empty')    
            return
        else:
            while current.next != self.head:
                result.add(current.data)
                current = current.next
            # Add the tail of the original list to the cloned list
            result.add(current.data)
            return result

    # Displays all the nodes in the list    
    def display(self):    
        current = self.head    
        if self.head is None:    
            print('List is empty')    
            return    
        else:     
            #Prints each node by incrementing pointer    
            print(current.data)    
            while current.next != self.head:    
                current = current.next    
                print(current.data)


if __name__ == '__main__':
    cll = CircularLinkedList()
    for i in range(5, 0, -1):
        cll.add(i)
    print('\nOriginal Circular Linked List\n')
    cll.display()
    print('-------')
    clone = cll.clone()
    print('\nCloned Circular Linked List\n')
    clone.display()
    print('-------')
