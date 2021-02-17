import string

lst = input('Input:')
lst2 = list(lst)

count = 0 
i = 0

for i in range(len(lst)):
	if lst2[i] == ' ':
		lst2[i] = '%' #python does not support item assignment in String
		continue
	else:
		count = count+1
result = ''.join(map(str,lst2))
print (result)
print (count)


