# Chapter 2 Linked Lists
# Interview Questions 2.3
# Delete middle node:
# Implement an algorithm to delete a node in the middle

import os
from LinkedList import LinkedList
from LinkedList import LinkedListNode

def delete_middle_node(node):
	node.value = node.next.value
	node.next = node.next.next

ll = LinkedList()
ll.add_multiple([1, 2, 3, 4])
middle_node = ll.add(5)
ll.add_multiple([7, 8, 9])

print(ll)
delete_middle_node(middle_node)
print(ll)