#program for coordinate compession


def coor_comp (lst):
	lst = list(dict.fromkeys(lst))
	new = sorted(lst)
	for i in range(len(lst)):
		lst[i] = new.index(lst[i])
	print("compressed coordinates are :", lst)
	return

a = [2,6,1,4]
coor_comp(a)
print("initial list is :", a)

