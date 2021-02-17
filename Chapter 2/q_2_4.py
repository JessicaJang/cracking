# Chapter 2 Linked Lists
# Interview Questions 2.4
# Partition: Write code to partition a linked list around a value x
# 			 such that all nodes less than x come before all nodes
#			 greater than or equal to x. if x is contained within the
#			 list, the values of x only need to be after the elements
#			 less than x. The partition elements x can appear anywhere
#			 in the right partition; it does not need to appear between
#			 the left and right partitions.

from LinkedList import LinkedList
from LinkedList import LinkedListNode


def partition(ll, x):
    current = ll.tail = ll.head

    while current:
        nextNode = current.next
        current.next = None
        if current.value < x:
            current.next = ll.head
            ll.head = current
        else:
            ll.tail.next = current
            ll.tail = current
        current = nextNode
        
    # Error check in case all nodes are less than x
    if ll.tail.next is not None:
        ll.tail.next = None


ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
partition(ll, ll.head.value)
print(ll)
