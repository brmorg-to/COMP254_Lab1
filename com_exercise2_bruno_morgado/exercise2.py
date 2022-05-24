# Student# 301-154-898
#Student: Bruno Cantanhede Morgado

import os
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath (__file__) ) ) )

from com_exercise1_bruno_morgado.exercise1 import  LinkedList

#Concatenate two Singly Linked Lists
def concat_two_linked_lists(l1, l2):

    if l1.head is not None:
        concat_list = l1.copy()
        actual_node = concat_list.head
    # If the head is NULL, there's nothing to concatenate
    else:
        return

    while actual_node.next_node is not None:
        actual_node = actual_node.next_node

    if l2.head is not None:
        new_node = l2.head
        # Use the insert_end method to insert the first node of L2 to the end of L1
        concat_list.insert_end(new_node)
        new_node = new_node.next_node
        # Loop through L2 and append each node to the end of the concat_list
        while new_node.next_node is not None:
            concat_list.insert_end(new_node)
            new_node = new_node.next_node
        concat_list.insert_end(new_node)

    concat_list.traverse()


if __name__ == '__main__':

    l1 = LinkedList()

    for i in range(5, 0, -1):
        l1.insert_start(i)

    print('List 1')
    l1.traverse()
    print('------------------------------------------------------------------')

    l2 = LinkedList()

    for i in range(10, 5, -1):
        l2.insert_start(i)

    print('List 2')
    l2.traverse()
    print('------------------------------------------------------------------')

    print('Concatenated Linked List')
    concat_two_linked_lists(l1, l2)
