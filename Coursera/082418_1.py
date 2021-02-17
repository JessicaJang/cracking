def pig_latin(word):
	if word[0]== 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
		print(word+'way')
	else:
		consonant_ver = word[1:]+word[0]+'ay'
		print(consonant_ver)

	return

pig_latin('pig')
pig_latin('owl')




