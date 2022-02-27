
lst = [1,2,3,4, 5 ,6,7,8,9]

def find_item_index(start, end, item):
	mid = (end - start)//2 + start
	mid_item = lst[mid]
	if item == mid_item:
		return mid

	if item < mid_item:
		return find_item_index(start, mid-1, item)

	if item > mid_item:
		return find_item_index(mid+1, end, item)
	return -1
	


index = find_item_index(0, len(lst), 4)
print("Result ", index)

