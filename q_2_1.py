# Chapter 2 Linked Lists
# Interview Questions 2.1
# Write code to remove duplicates from an unsorted linked list

import os

class ListNode(object):
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

def remove_dups(head):
	if head is None:
		return

	current = head
	hashMap = set([current.val])

	while current.next:
		if current.next.val in hashMap:
			current.next = current.next.next
		else:
			hashMap.add(current.next.val)
			current = current.next
	return head

head = ListNode(20)
head.next = ListNode(70)
head.next.next = ListNode(10)
head.next.next.next = ListNode(70)

ans = remove_dups(head)
track = head
while track.next:
	print(track.val)
	track = track.next
print(track.val)




