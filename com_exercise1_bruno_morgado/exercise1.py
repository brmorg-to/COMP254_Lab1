# Student# 301-154-898
#Student: Bruno Cantanhede Morgado

class _Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return str(self.data)


class LinkedList:

    def __init__(self):
        # First node of the linked list
        self.head = None
        self.num_of_nodes = 0

    # Insert a node at the start of the LinkedList
    def insert_start(self, data):
        self.num_of_nodes += 1
        new_node = _Node(data)

        # If head is NULL
        if self.head is None:
            self.head = new_node
        # When LInked List is not Empty
        else:
            # we have to update the references
            new_node.next_node = self.head
            self.head = new_node

    # Insert nodes at the end of the list
    def insert_end(self, data):
        self.num_of_nodes += 1
        new_node = _Node(data)

        # check if the linked list is empty
        if self.head is None:
            self.head = new_node
        else:
            # When the linked list is not empty
            actual_node = self.head

            # Traverse the entire list
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node

            # actual_node is the last node: so we insert the new_node right after the actual_node
            actual_node.next_node = new_node

    # Return the number of nodes of a List
    def size_of_list(self):
        return self.num_of_nodes

    # Traverse and Print the list
    def traverse(self):

        actual_node = self.head

        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.next_node

    # Remove a node
    def remove(self, data):

        # the list is empty
        if self.head is None:
            return

        actual_node = self.head
        # Store a reference to the previous node
        previous_node = None

        # search for the item we want to remove (data)
        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node

        # search miss
        if actual_node is None:
            return

        # When the head node is the one to be removed
        if previous_node is None:
            self.head = actual_node.next_node
        else:
            # remove an internal node by updating the pointers
            previous_node.next_node = actual_node.next_node

    def swap_two_nodes(self, x, y):

        if self.head is None:
            return
        # If the values are equivalent, return
        if (x == y):
            return

        # Search for x (keep track of prevX and CurrX)
        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next_node

        # Search for y (keep track of prevY and currY)
        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next_node

        # If either x or y is not present, nothing to do
        if currX == None or currY == None:
            return
        # If x is not the head of linkedList
        if prevX != None:
            prevX.next_node = currY
        else:  # make y the new head
            self.head = currY

        # If y is not head of linked list
        if prevY != None:
            prevY.next_node = currX
        else:  # make x the new head
            self.head = currX

         # Swap next pointers
        temp = currX.next_node
        currX.next_node = currY.next_node
        currY.next_node = temp

    # Clone a linked List
    def copy(self):
        result = LinkedList()
        buffer = self.head
        while buffer.next_node != None:
            result.insert_end(buffer.data)
            buffer= buffer.next_node
        result.insert_end(buffer.data)
        return result

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_end(10)
    linked_list.insert_start(20)
    linked_list.insert_start(30)
    linked_list.insert_end('Adam')
    linked_list.insert_end(7.5)
    linked_list.traverse()
    print('-------')
    linked_list.swap_two_nodes(10, 30)
    linked_list.traverse()
    print('-------')
    linked_list.swap_two_nodes(20, 'Adam')
    linked_list.traverse()
