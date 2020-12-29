import os

def permutation(s):
	if len(s) == 1:
		return s

	perm_list = []
	for a in s:
		remain = [x for x in s if x!=a]
		z = permutation(remain)

		for t in z:
			perm_list.append(a + t)

	return perm_list

def permutation2(s, num):
	if len(s) == 1:
		return s

	perm_list = []
	for a in s:
		remain = []
		for i in range(len(s))

res = permutation('abc')
print(res)
