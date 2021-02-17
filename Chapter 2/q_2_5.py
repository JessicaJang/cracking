# Chapter 2 Linked Lists
# Interview Questions 2.5
# Sum Lists: You have two numbers represented by a linked list,
# 			where each node contains a single digit. The digits
#			are stored in reverse order, such that the 1's digit
#			is at the head of the list. Write a function that 
#			adds the two numbers and returns the sum as a linked list

from LinkedList import LinkedList
from LinkedList import LinkedListNode

# sumList function
def sumList(l1, l2):
	# edge case
	if l1.head is None and l2.head is None:
		return 0
	elif l1.head is None:
		return l2
	elif l2.head is None:
		return l1

	cur1 = l1.head
	cur2 = l2.head

	res = LinkedList()
	c = value = 0

	while (cur1 or cur2):
		value = value + c

		if cur1:
			value += cur1.value
			cur1 = cur1.next

		if cur2:
			value += cur2.value
			cur2 = cur2.next

		c = value // 10
		value = value % 10

		res.add(value)
		value = 0

	if c == 1:
		res.add(1)

	# edge case
	tmp2 = res.head

	while (tmp2.next != res.tail):
		tmp2 = tmp2.next

	if (res.tail.value == 0) and (res.__len__() > 1):
		tmp2.next = None

	return res


# main block starts here

list1 = LinkedList()
list1.generate(4, 0, 9)

list2 = LinkedList()
list2.generate(3, 0, 9)

print(list1)
print(list2)
print(sumList(list1, list2))