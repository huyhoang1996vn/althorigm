cake = 'donut'


def reserve_string(item):
	if len(item) < 1:
		return ""
	return reserve_string(item[1:]) + item[0]

reserve = reserve_string(cake)
print("Result: ", reserve) 