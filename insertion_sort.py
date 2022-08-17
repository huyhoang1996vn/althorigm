lst = [2,5,3,1,6,4]

list_sorted = []
for i in range(0, len(lst)):
	key = lst[i]
	len_list_sorted = len(list_sorted)
	print("==== len_list_sorted ", len_list_sorted)
	print("==== key ", key)
	list_sorted.append(key)
	for j in range(len_list_sorted, -1, -1):
		print("==== list_sorted[j] ", list_sorted[j])
		if key < list_sorted[j]:
			list_sorted[j+1] = list_sorted[j]
			list_sorted[j] = key
		print(list_sorted)
		




print("=== list_sorted ", list_sorted)

