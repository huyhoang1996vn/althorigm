lst = [2,5,3,1,6,4]

for index in range(len(lst)-1):
	for index_next in range(index+1, len(lst)):
		if lst[index_next] < lst[index]:
			lst[index], lst[index_next] = lst[index_next], lst[index]


print("=== lst ", lst)

