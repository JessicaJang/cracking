# Chapter 2 Linked Lists
# Interview Questions 2.2
# Implement an algorithm to find the kth to last element of a singly linked list

import os
from LinkedList import LinkedList

def kth_to_last(node, k):
	runner = current = node.head

	for i in range(0, k):
		if runner is None:
			return None
		runner = runner.next

	while runner:
		current = current.next
		runner = runner.next

	return current

sol = LinkedList()
sol.generate(10, 0, 99)
print(sol)
print(kth_to_last(sol, 2))




