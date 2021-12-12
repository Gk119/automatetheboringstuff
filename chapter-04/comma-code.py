def formatlist(ls):
	if len(ls) == 0:
		return ""

	str = ""
	for x in range(len(ls) - 1):
		str += ls[x] 
		if x != len(ls) - 2:
			str += ", "
	
	if len(ls) > 1:
		str += " and "

	str += ls[len(ls) - 1]
	return str

l1 = ['apples','bananas','oranges','watermelon','mango','strawberry']
l2 = ['apples']
l3 = []
print(formatlist(l1))
print(formatlist(l2))
print(formatlist(l3))

